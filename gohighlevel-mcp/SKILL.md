---
name: gohighlevel-mcp
description: Manage GoHighLevel via MCP for individual actions (contacts/conversations/opportunities/pipelines) and CRM triage workflows. Use when user asks to check inbox, reply to unresponded leads, or update pipeline stages.
metadata:
  openclaw:
    requires:
      env:
        - GHL_PIT_TOKEN
        - GHL_LOCATION_ID
---

# GoHighLevel MCP

Use this skill for GHL CRM operations through the MCP endpoint.

## Credentials
- Use `$GHL_PIT_TOKEN` and `$GHL_LOCATION_ID` only.
- Never hardcode keys in files or chat.
- Credentials must live in `~/.openclaw/openclaw.json` under `skills.entries.gohighlevel-mcp.env`.
- Do **not** use `$GHL_API_KEY`/`$GHL_MCP_API_KEY` for this skill path.
- Source of truth is `skills.entries.gohighlevel-mcp.env`; if `config/mcporter.json` differs, sync `Authorization` + `locationId` from source of truth before any live call.

## Workflow
1. Validate credentials present.
- Command: `test -n "$GHL_PIT_TOKEN" && test -n "$GHL_LOCATION_ID"`
- Success: exit code 0.
- Failure: request missing value(s) from user.

2. Preflight config sync check (required for mcporter calls).
- Verify `config/mcporter.json` uses the same bearer token + location as `~/.openclaw/openclaw.json` → `skills.entries.gohighlevel-mcp.env`.
- If mismatch: update `config/mcporter.json` first, then continue.

3. Connectivity test (non-destructive).
- Command:
`curl -sS -X POST https://services.leadconnectorhq.com/mcp/ -H "Authorization: Bearer $GHL_PIT_TOKEN" -H "locationId: $GHL_LOCATION_ID" -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" -A "Mozilla/5.0" -d '{"jsonrpc":"2.0","id":"ping","method":"tools/list","params":{}}'`
- Success: SSE response with `data: {"result":{"tools":[...]}}`.
- Failure: 401/403/406/4xx or timeout.

4. Individual action mode.
- Run one MCP tool call for requested task (contacts, conversations, opportunities, pipelines).
- Use live tool schemas from `tools/list` before first call in session.
- Success: API returns data or confirms mutation.
- Failure: schema mismatch or auth/location error.

5. Triage workflow mode.
- Sequence: list conversations → detect unresponded inbound → draft/send reply (with user-approved tone) → evaluate/update opportunity stage.
- Dry-run first, then ask for approval before live message/stage updates.
- Success: report counts + per-contact actions.
- Failure: partial completion must be reported clearly.

## REST API Fallback
If MCP returns errors or is unreachable, use proven REST commands in:
`references/rest-fallbacks.md` — 12 core endpoints, all live-verified with correct headers/params.

## Error Handling
| Error | Cause | Fix |
|---|---|---|
| 401 Unauthorized | Bad/expired PIT | Replace PIT and retest |
| 403/404 location | Wrong Location ID | Confirm sub-account Location ID |
| Invalid params | Tool schema drift | Refresh `tools/list`, adapt payload |
| Send blocked | Missing channel permissions | Skip send, log contact for manual follow-up |

## Gotchas
- Always run non-destructive test before workflow run.
- Do dry-run before any outbound message updates.
- Don't promise workflow enrollment automation unless verified live.
- Keep reply tone short, human, and context-grounded.
- MCP endpoint requires `Accept: application/json, text/event-stream` header or returns 406.
- Cloudflare blocks default python UA; include a browser-like `User-Agent` header.
- Responses come as SSE (`event: message\ndata: {...}`); parse the `data:` line as JSON.
