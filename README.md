# 🤖 OpenClaw Skills — Toniolo AI Agency

[![Skills](https://img.shields.io/badge/skills-21-blue)](https://github.com/katetonioloai/-openclaw-skills)
[![Platform](https://img.shields.io/badge/platform-OpenClaw-black)](https://github.com/openclaw/openclaw)
[![Status](https://img.shields.io/badge/status-production-green)](https://x.com/toniolo32292)
[![Commission](https://img.shields.io/badge/custom%20skills-DM%20us-orange)](https://x.com/toniolo32292)

> Production-ready skills and agents for the [OpenClaw](https://github.com/openclaw/openclaw) platform — built and battle-tested by Toniolo AI Agency.

**→ Need a custom skill? DM [@toniolo32292](https://x.com/toniolo32292) on X**

---

## 🏗️ What We Build

We build two types of things for OpenClaw:

| Type | What it is | Examples |
|------|-----------|---------|
| **Skills** | Packaged tools an agent can use | TikTok automation, CRM integration, scraping |
| **Agents** | Specialized AI team members | Researcher, Developer, Social Media Manager |

Everything in this repo is running in production today.

---

## 🛠️ Skills

### 🎬 [tiktok-text-overlay](./tiktok-text-overlay)
Add branded text overlays to TikTok videos for Shop/BOF campaigns.
- PILL style (deal boxes) + HOOK style (big screen text)
- Pure Python + ffmpeg, zero extra deps
- Used in active affiliate campaigns generating daily commissions

### 📱 [tiktok-draft](./tiktok-draft.skill)
Push videos to TikTok Studio drafts via Playwright — no API approval needed.
- Session-authenticated, bypasses unaudited app restrictions
- Caption + hashtags + draft in one command

### 🔍 [apify-scraper](./apify-scraper)
Run 4,000+ Apify actors from any OpenClaw agent.
- TikTok, Instagram, Google Maps, Amazon, and thousands more
- Structured JSON output, one skill covers everything

### 📊 [gohighlevel-mcp](./gohighlevel-mcp)
Full GoHighLevel CRM control from your agent.
- Contacts, conversations, opportunities, pipelines
- CRM triage: check inbox → draft reply → update stage

### ✍️ [cashclaw-content-writer](./cashclaw-content-writer)
AI-powered blog posts, social content, and email newsletters.
- SEO-optimized, publish-ready copy
- Follows proven content frameworks

### 🎯 [cashclaw-lead-generator](./cashclaw-lead-generator)
Systematic B2B lead research and qualification.
- Structured lead lists with contact info and scoring
- Multi-source research pipeline

### 🔎 [cashclaw-seo-auditor](./cashclaw-seo-auditor)
Comprehensive SEO audits with actionable reports.
- Technical SEO, on-page, off-page, performance
- Prioritized recommendations

### 📣 [cashclaw-social-media](./cashclaw-social-media)
Content calendars and platform-specific posts.
- Instagram, X, LinkedIn, TikTok, Facebook
- Analytics tracking + scheduling

### 🎙️ [ghl-voice-agent](./ghl-voice-agent)
Create and manage GoHighLevel AI Voice Agents via REST API.
- AI receptionist setup in minutes
- Call logs and transcript management

---

## 🤖 Agent Team

A fully operational 5-agent AI team running in production. Each agent has a defined role, personality, memory system, and communication channel.

### [🏛️ Multi-Agent Architecture](./multi-agent-team)
How the full team is structured and coordinated.

```
Patricia (human CEO)
        ↕ Telegram
    Kate (AI CEO / Orchestrator)
        ├── Yang  → builds, codes, ships
        ├── Grey  → researches, analyzes  
        ├── Bailey → CRM, growth, outreach
        └── Lexie → social, content, TikTok
```

### Individual Agent Docs
| Agent | Role | Specialization |
|-------|------|---------------|
| [🔍 Grey](./agent-grey) | Researcher | Market intel, competitive analysis, trend spotting |
| [⚡ Yang](./agent-yang) | Developer | Full-stack, APIs, automation, production builds |
| [📈 Bailey](./agent-bailey) | Growth + GHL | CRM ops, lead outreach, client acquisition |
| [📱 Lexie](./agent-lexie) | Social + Content | TikTok, Instagram, X content with brand voice |

---

## 💼 Commission a Custom Skill

Have a tool, API, or workflow you want your OpenClaw agent to master?

We scope → build → test → document → deliver.

**Typical turnaround: 1–3 days**

**→ DM [@toniolo32292](https://x.com/toniolo32292) on X to get started**

---

## 📦 Using a Skill

```bash
# 1. Clone or download the skill folder
git clone https://github.com/katetonioloai/-openclaw-skills

# 2. Drop the skill folder into your OpenClaw workspace
cp -r -openclaw-skills/tiktok-text-overlay ~/your-workspace/skills/

# 3. Your agent can now use it — no config needed
```

OpenClaw agents auto-discover skills in the workspace. The agent reads `SKILL.md` to understand what it can do.

---

*Toniolo AI Agency · Building agent infrastructure since 2026 · [Follow our journey](https://x.com/toniolo32292)*

---

## 🔧 Utility Skills

### 🎙️ [openai-whisper](./openai-whisper)
Local speech-to-text — transcribe audio files with no API key needed.
- Runs fully local via Whisper CLI
- Supports ogg, mp3, mp4, wav and more
- Used in production to transcribe every voice message

### 𝕏 [xurl](./xurl)
Full X (Twitter) API access — post, reply, search, DM, upload media.
- OAuth1 + OAuth2 support
- Post with images, reply to threads, search mentions
- Powers automated X posting pipeline

### 📝 [summarize](./summarize)
Summarize URLs, YouTube videos, podcasts, and local files.
- Extract transcripts from YouTube
- Summarize articles and long-form content
- No API key required for most sources

### 🎞️ [video-frames](./video-frames)
Extract frames and short clips from videos using ffmpeg.
- Screenshot any frame from a video
- Cut clips by timestamp
- Batch frame extraction

### 🐙 [github](./github)
GitHub operations via `gh` CLI — issues, PRs, CI, code review.
- Check PR status and CI runs
- Create and comment on issues
- Query any GitHub API endpoint

### 🌤️ [weather](./weather)
Current weather and forecasts for any location — no API key.
- Powered by wttr.in and Open-Meteo
- Supports any city or coordinates
- Instant, no setup

### 💻 [coding-agent](./coding-agent)
Delegate complex coding tasks to Codex or Claude Code agents.
- Spawn isolated coding sessions for big features
- Review PRs in temp directories
- Refactor large codebases autonomously
