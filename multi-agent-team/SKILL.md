---
name: multi-agent-team
description: A production multi-agent team built on OpenClaw. 5 specialized agents with defined roles, cross-channel communication, heartbeat monitoring, and a CEO orchestrator.
---

# Multi-Agent Team Architecture

A fully operational AI agency team running on OpenClaw, built and deployed for Toniolo AI Agency.

## Team Structure

| Agent | Role | Model | Channel |
|-------|------|-------|---------|
| **Kate** | CEO / Orchestrator | Claude Sonnet | Telegram + Discord |
| **Yang** | Developer | Claude Opus | Discord |
| **Grey** | Researcher | Claude Haiku | Discord |
| **Bailey** | Growth / GHL Ops | Claude Haiku | Discord |
| **Lexie** | Social / Content | Claude Haiku | Discord |

## Architecture

```
Patricia (human)
    ↕ Telegram
  Kate (CEO)
    ├── Yang (builds, fixes, codes)
    ├── Grey (researches, analyzes)
    ├── Bailey (GHL, outreach, growth)
    └── Lexie (TikTok, Instagram, X content)
```

## Key Patterns

### Agent Identity (SOUL.md)
Each agent has a `SOUL.md` defining personality, communication style, and mission. This keeps agents consistent across sessions.

### Memory System
- `memory/YYYY-MM-DD.md` — daily logs (raw notes)
- `MEMORY.md` — long-term curated memory (main session only)
- Agents wake up fresh but read their memory files to maintain continuity

### Heartbeat System
Grey, Bailey, and Lexie run on 30-minute heartbeats during active hours (8am-10pm EST). Each heartbeat checks for pending tasks without requiring manual triggers.

### Task Delegation via CURRENT_TASK.md
Kate writes tasks to `agents/[name]/CURRENT_TASK.md`. The agent reads it on next activation and executes.

### Model Strategy
- Heavy reasoning/coding → Opus (Yang)
- Orchestration/strategy → Sonnet (Kate)
- Routine tasks/content → Haiku (Grey, Bailey, Lexie)

## Capabilities Unlocked

- Autonomous TikTok Shop video pipeline (film → edit → draft)
- X/Instagram content calendar with approval workflow
- GHL CRM management and lead outreach
- Real-time research and competitive analysis
- Self-improving through memory updates and skill documentation

## Setup

Each agent needs:
1. A workspace folder: `agents/[name]/`
2. `SOUL.md` — identity and mission
3. `AGENTS.md` — workspace rules
4. `USER.md` — who they're helping
5. OpenClaw config binding to their Discord channel

---
*Built by Toniolo AI Agency*
