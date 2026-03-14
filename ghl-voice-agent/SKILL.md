---
name: ghl-voice-agent
description: Create, update, delete, and list GoHighLevel AI Voice Agents via the GHL Voice AI REST API. Use when asked to create a new GHL voice agent, build a demo AI receptionist, update an existing voice agent's prompt or settings, list all agents, delete an agent, or pull call logs and transcripts for any GHL voice agent. Credentials are in ~/.secrets/agents.env.
---

# GHL Voice Agent Skill

Create and manage GHL AI Voice Agents using the Voice AI REST API.

## Credentials

```bash
source ~/.secrets/agents.env
# Provides: $GHL_API_TOKEN and $GHL_LOCATION_ID
```

## Workflow

### Create a Voice Agent

Run the creation script with required parameters:

```bash
bash /Users/tonioloai/.openclaw/workspace/skills/ghl-voice-agent/scripts/create_voice_agent.sh \
  --name "Agent Name" \
  --business "Business Name" \
  --greeting "Thank you for calling..." \
  --prompt "You are a receptionist for..."
```

Optional flags:
- `--phone "+19412975651"` — assign a phone number (must not be claimed by another active agent)
- `--voice "uYXf8XasLslADfZ2MB4u"` — ElevenLabs voice ID
- `--duration 300` — max call duration in seconds (default 300)

The script prints the new agent ID on success.

### Update an Agent

```bash
source ~/.secrets/agents.env
curl -s -X PATCH "https://services.leadconnectorhq.com/voice-ai/agents/$AGENT_ID" \
  -H "Authorization: Bearer $GHL_API_TOKEN" \
  -H "Version: 2021-04-15" \
  -H "Content-Type: application/json" \
  -d "{\"locationId\": \"$GHL_LOCATION_ID\", \"agentPrompt\": \"New prompt here\"}"
```

### List All Agents

```bash
source ~/.secrets/agents.env
curl -s "https://services.leadconnectorhq.com/voice-ai/agents?locationId=$GHL_LOCATION_ID" \
  -H "Authorization: Bearer $GHL_API_TOKEN" \
  -H "Version: 2021-04-15" | python3 -m json.tool
```

### Pull Call Logs

```bash
source ~/.secrets/agents.env
curl -s "https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs?locationId=$GHL_LOCATION_ID&pageSize=10&sortBy=createdAt&sort=descend" \
  -H "Authorization: Bearer $GHL_API_TOKEN" \
  -H "Version: 2021-04-15" | python3 -m json.tool
```

Filter by agent: append `&agentId=YOUR_AGENT_ID`

### Get Single Call Log (with full transcript)

```bash
source ~/.secrets/agents.env
curl -s "https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs/$CALL_ID?locationId=$GHL_LOCATION_ID" \
  -H "Authorization: Bearer $GHL_API_TOKEN" \
  -H "Version: 2021-04-15" | python3 -m json.tool
```

### Delete an Agent

```bash
source ~/.secrets/agents.env
curl -s -X DELETE "https://services.leadconnectorhq.com/voice-ai/agents/$AGENT_ID?locationId=$GHL_LOCATION_ID" \
  -H "Authorization: Bearer $GHL_API_TOKEN" \
  -H "Version: 2021-04-15"
```

## Key Rules

- **Phone numbers:** A number can only be attached to one active agent. To reassign, PATCH the existing agent with `"inboundNumbers": []` first.
- **No website widgets** unless Patricia explicitly approves.
- **Demo agents** stay inside GHL only — never connect to a client's live website without approval.
- After creating, report back: agent ID, agent name, and phone number (if assigned).

## Full API Reference

See `references/api.md` for all fields, voice IDs, and response schemas.
