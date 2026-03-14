---
name: apify-universal-scraper
description: Run any of 4,000+ Apify actors to scrape websites and extract structured data. Covers Instagram, Facebook, TikTok, YouTube, Google Maps, Google Search, Amazon, travel sites, and more. Use when the user asks to scrape, extract data, find leads, monitor brands, analyze competitors, discover influencers, or pull structured data from any website.
metadata: {"openclaw":{"emoji":"🕷️","requires":{"env":["APIFY_TOKEN"]}}}
---

# Apify Universal Scraper

Run any Apify actor using native OpenClaw tools. No scripts needed.

## Method 1: Webhook mode (preferred)

Start the actor and let Apify notify OpenClaw when done. No polling. Use this by default.

### Start the actor with webhook

**CRITICAL: Apify ad-hoc webhooks MUST be a base64-encoded query parameter on the URL. They are NOT part of the actor input body. Apify silently ignores webhooks in the body.**

#### Step 1: Build the base64 webhook string
```
WEBHOOK_JSON='[{"eventTypes":["ACTOR.RUN.SUCCEEDED"],"requestUrl":"'"$OPENCLAW_WEBHOOK_URL"'/hooks/agent","headersTemplate":"{\\"Authorization\\":\\"Bearer '"$OPENCLAW_HOOKS_TOKEN"'\\"}","payloadTemplate":"{\\"message\\":\\"Apify actor finished. Dataset: {{resource.defaultDatasetId}}. Fetch results and summarize for user.\\",\\"name\\":\\"Apify\\"}","shouldInterpolateStrings":true}]'
WEBHOOKS_B64=$(echo -n "$WEBHOOK_JSON" | base64 | tr -d '\n')
```

#### Step 2: Start the actor with webhook as query param
```
curl -s -X POST "https://api.apify.com/v2/acts/ACTOR_ID/runs?token=$APIFY_TOKEN&webhooks=$WEBHOOKS_B64" \
  -H "Content-Type: application/json" \
  -d 'ACTOR_INPUT_JSON_ONLY'
```

The `-d` body contains ONLY the actor input (searchStringsArray, locationQuery, etc). NO webhooks in the body.

ACTOR_ID format: use `author~actor` (tilde, not slash). Example: `compass~crawler-google-places`

The env vars `$OPENCLAW_WEBHOOK_URL` and `$OPENCLAW_HOOKS_TOKEN` are available at runtime. Never hardcode these values.

After starting, tell the user the scrape is running and they will be notified when results are ready. Do NOT poll. OpenClaw will receive the webhook and start a new agent turn automatically.

### When the webhook arrives

OpenClaw will wake you with a message containing the dataset ID and instructions. Use `web_fetch` to get the results:
```
https://api.apify.com/v2/datasets/DATASET_ID/items?token=$APIFY_TOKEN&clean=true&limit=10
```

Summarize the results and deliver to the user.

## Method 2: Polling mode (fallback)

Use this only if the webhook is not configured or the actor finishes very quickly (under 30 seconds).

### Step 1: Start the actor

Use `exec` with `curl`:
```
curl -s -X POST "https://api.apify.com/v2/acts/ACTOR_ID/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d 'INPUT_JSON'
```

Save `data.id` (runId) and `data.defaultDatasetId` (datasetId) from the response.

### Step 2: Check run status

Use `web_fetch`:
```
https://api.apify.com/v2/actor-runs/RUN_ID?token=$APIFY_TOKEN
```

Look at `data.status`:
- `RUNNING` — wait 15-30 seconds and check again.
- `SUCCEEDED` — go to Step 3.
- `FAILED` / `TIMED-OUT` / `ABORTED` — tell the user and link to: `https://console.apify.com/actors/runs/RUN_ID`

### Step 3: Fetch results

Use `web_fetch`:
```
https://api.apify.com/v2/datasets/DATASET_ID/items?token=$APIFY_TOKEN&clean=true&limit=10
```

## Rules

1. NEVER dump raw JSON to the user. Summarize results in a readable format.
2. After starting a run, tell the user it is in progress.
3. In polling mode, wait 15-30 seconds between checks. Do not poll more than 20 times.
4. If a run takes too long in polling mode, give the user the runId and offer to check later.
5. Use `&fields=title,address,totalScore,phone,website` on dataset URLs to reduce payload size when you know which fields matter.
6. For checking old runs or datasets the user provides, go directly to status check or dataset fetch.
7. Default to webhook mode. Only use polling mode if webhook is unavailable.

## Common actors and inputs

### Google Maps (businesses, restaurants, services)
- Actor: `compass~crawler-google-places`
- Input: `{"searchStringsArray":["QUERY"],"locationQuery":"CITY, STATE","maxCrawledPlacesPerSearch":10}`
- Key fields: `title, address, totalScore, phone, website, url`

### Instagram profiles
- Actor: `apify~instagram-profile-scraper`
- Input: `{"usernames":["username1","username2"]}`

### Google Search
- Actor: `apify~google-search-scraper`
- Input: `{"queries":"search terms","maxPagesPerQuery":1}`

### TikTok
- Actor: `clockworks~tiktok-scraper`
- Input: `{"hashtags":["hashtag1"],"resultsPerPage":10}`

For the full actor catalog with 55+ actors organized by platform, see `{baseDir}/references/actor-catalog.md`.

## Looking up actor input schemas

If you are unsure what input an actor expects, fetch its schema with `web_fetch`:
```
https://api.apify.com/v2/acts/ACTOR_ID?token=$APIFY_TOKEN
```

Check `data.defaultRunInput` for the expected input format.
