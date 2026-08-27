#!/usr/bin/env python3
"""Collect weekly, aggregate GitHub contribution metrics.

The script intentionally stores aggregates rather than usernames or comment bodies.
It uses only the Python standard library and GitHub REST/GraphQL APIs.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPO = os.environ.get("GITHUB_REPOSITORY", "meunier-jc/authentic-fluency")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
DAYS = int(os.environ.get("METRICS_DAYS", "7"))
OUT_DIR = Path(os.environ.get("METRICS_OUT_DIR", "metrics"))
API = "https://api.github.com"

if not TOKEN:
    print("GITHUB_TOKEN is required", file=sys.stderr)
    sys.exit(2)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def request_json(url: str, method: str = "GET", body: dict | None = None) -> dict | list:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "authentic-fluency-weekly-metrics",
    }
    data = json.dumps(body).encode() if body is not None else None
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(req, timeout=30) as response:
            return json.load(response)
    except (HTTPError, URLError) as exc:
        print(f"GitHub API request failed: {url}: {exc}", file=sys.stderr)
        raise


def paged_rest(path: str, params: str = "") -> list[dict]:
    values: list[dict] = []
    page = 1
    while True:
        suffix = f"&page={page}" if params else f"?page={page}"
        url = f"{API}{path}{params}{suffix}"
        batch = request_json(url)
        if not isinstance(batch, list):
            raise ValueError(f"Expected list from {url}")
        values.extend(batch)
        if len(batch) < 100:
            return values
        page += 1


def first_response_hours(number: int, created: datetime, kind: str) -> float | None:
    comments = paged_rest(f"/repos/{REPO}/issues/{number}/comments", "?per_page=100")
    for comment in comments:
        timestamp = parse_date(comment.get("created_at"))
        if timestamp and timestamp >= created:
            return round((timestamp - created).total_seconds() / 3600, 2)
    return None


def discussions_since(start: datetime) -> dict:
    query = """
    query($owner:String!, $name:String!, $after:String) {
      repository(owner:$owner, name:$name) {
        discussions(first:100, after:$after, orderBy:{field:CREATED_AT, direction:DESC}) {
          pageInfo { hasNextPage endCursor }
          nodes { createdAt author { login } category { name } }
        }
      }
    }
    """
    owner, name = REPO.split("/", 1)
    results: list[dict] = []
    cursor = None
    while True:
        payload = request_json(
            f"{API}/graphql",
            method="POST",
            body={"query": query, "variables": {"owner": owner, "name": name, "after": cursor}},
        )
        if payload.get("errors"):
            raise RuntimeError(payload["errors"])
        node = payload["data"]["repository"]["discussions"]
        for item in node["nodes"]:
            created = parse_date(item.get("createdAt"))
            if created and created >= start:
                results.append(item)
            elif created and created < start:
                return {
                    "opened": len(results),
                    "categories": sorted({(x.get("category") or {}).get("name") for x in results if x.get("category")}),
                }
        if not node["pageInfo"]["hasNextPage"]:
            break
        cursor = node["pageInfo"]["endCursor"]
    return {
        "opened": len(results),
        "categories": sorted({(x.get("category") or {}).get("name") for x in results if x.get("category")}),
    }


def collect() -> dict:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=DAYS)
    start_s, end_s = iso(start), iso(end)

    issues = paged_rest(f"/repos/{REPO}/issues", f"?state=all&since={start_s}&per_page=100")
    issues = [x for x in issues if not x.get("pull_request")]
    pulls = paged_rest(f"/repos/{REPO}/pulls", "?state=all&sort=created&direction=desc&per_page=100")
    pulls = [x for x in pulls if (created := parse_date(x.get("created_at"))) and created >= start]

    opened_issues = [x for x in issues if (created := parse_date(x.get("created_at"))) and created >= start]
    closed_issues = [x for x in issues if (closed := parse_date(x.get("closed_at"))) and closed >= start]
    merged_pulls = [x for x in pulls if (merged := parse_date(x.get("merged_at"))) and merged >= start]

    contributors: set[str] = set()
    first_time = 0
    response_hours: list[float] = []
    for item in opened_issues + pulls:
        user = item.get("user") or {}
        if user.get("type") != "Bot" and user.get("login"):
            contributors.add(user["login"])
        if item.get("author_association") in {"FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR"}:
            first_time += 1
        created = parse_date(item.get("created_at"))
        if created:
            try:
                hours = first_response_hours(item["number"], created, "issue")
                if hours is not None:
                    response_hours.append(hours)
            except (HTTPError, URLError):
                pass

    discussions = discussions_since(start)
    avg_response = round(sum(response_hours) / len(response_hours), 2) if response_hours else None

    return {
        "repository": REPO,
        "period": {"start": start_s, "end": end_s, "days": DAYS},
        "issues": {"opened": len(opened_issues), "closed": len(closed_issues)},
        "pull_requests": {"opened": len(pulls), "merged": len(merged_pulls)},
        "discussions": discussions,
        "contribution": {
            "unique_non_bot_authors": len(contributors),
            "first_time_items": first_time,
            "items_with_first_response": len(response_hours),
            "average_first_response_hours": avg_response,
        },
        "notes": [
            "Counts exclude pull requests from the Issues total.",
            "Contributor names are not stored in the output.",
            "First-time status uses GitHub author_association and is an approximation.",
            "The report is descriptive and should not be used as an individual ranking.",
        ],
    }


def render_markdown(metrics: dict) -> str:
    p = metrics["period"]
    i, pr, d, c = metrics["issues"], metrics["pull_requests"], metrics["discussions"], metrics["contribution"]
    avg = f"{c['average_first_response_hours']} h" if c["average_first_response_hours"] is not None else "n/a"
    categories = ", ".join(d["categories"]) if d["categories"] else "n/a"
    return f"""# Weekly contribution metrics\n\n**Repository:** `{metrics['repository']}`  \n**Period:** `{p['start']}` → `{p['end']}`\n\nThis report contains aggregate project-level indicators. It is intended to improve onboarding and maintainer capacity, not to rank individual contributors.\n\n| Area | Metric | Value |\n|---|---|---:|\n| Issues | Opened | {i['opened']} |\n| Issues | Closed | {i['closed']} |\n| Pull requests | Opened | {pr['opened']} |\n| Pull requests | Merged | {pr['merged']} |\n| Discussions | Opened | {d['opened']} |\n| Discussions | Categories represented | {categories} |\n| Contribution | Unique non-bot authors | {c['unique_non_bot_authors']} |\n| Contribution | First-time items | {c['first_time_items']} |\n| Responsiveness | Items with a first response | {c['items_with_first_response']} |\n| Responsiveness | Average first-response time | {avg} |\n\n## Interpretation\n\nUse these values as a weekly baseline. Compare trends over at least 30, 60 and 90 days before changing the contribution guide or automation. Investigate separately any CI failures, link-check false positives or periods with no maintainer response.\n\n## Method notes\n\n- Issues, pull requests and comments are read through the GitHub API. Discussions are read through the GitHub GraphQL API.\n- Bot accounts are excluded from the unique-author count.\n- No usernames, comment bodies or personal data are written to the report.\n- A missing response is not treated as a zero-hour response.\n"""


if __name__ == "__main__":
    metrics = collect()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    (OUT_DIR / f"{stamp}.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    (OUT_DIR / "latest.md").write_text(render_markdown(metrics), encoding="utf-8")
    print(render_markdown(metrics))
