# OpenClaw Skills — Toniolo AI Agency

> Production-ready skills for the [OpenClaw](https://github.com/openclaw/openclaw) agent platform. Drop a skill folder into your workspace and your agent gains new capabilities instantly.

**Built and maintained by [Toniolo AI Agency](https://x.com/toniolo32292) · Custom skills on demand**

---

## How Skills Work

```
your-workspace/
└── skills/
    └── your-skill/
        ├── SKILL.md       ← agent reads this to learn how to use the skill
        └── scripts/       ← the actual tools/code
```

Your OpenClaw agent auto-discovers skills in the workspace. No configuration needed — just drop the folder and the agent knows what it can do.

---

## Skills in this Repo

### 🎬 tiktok-text-overlay
**Add branded text overlays to TikTok videos — production-ready for Shop/BOF campaigns.**

Two styles:
| Style | Description | Use case |
|-------|-------------|----------|
| `PILL` | Stacked red + white deal boxes, centered | Product deal urgency |
| `HOOK` | Large white text, black outline, top half of screen | Scroll-stop hooks |

```bash
# HOOK style
python3 scripts/overlay.py --style hook -i raw.mp4 -o final.mp4 \
  --text "Someone fcked up at TikTok cus today this foundation is on a triple discount..."

# PILL style
python3 scripts/overlay.py --style pill -i raw.mp4 -o final.mp4 \
  --top "DOUBLE DISCOUNT" --bottom "FINAL HOURS"
```

**Requirements:** Python 3, ffmpeg
**Used in:** Active TikTok Shop affiliate campaigns

---

### 📱 tiktok-draft
**Push videos directly to TikTok Studio drafts via Playwright — no unreliable Inbox API.**

```
Agent receives video → runs tiktok-draft → video appears in TikTok Studio → creator reviews & posts
```

- Session-authenticated browser automation
- Supports caption + hashtags
- Bypasses TikTok's unaudited app restrictions

---

### 🎬 Pipeline B — BOF Video Generator
**End-to-end TikTok Shop affiliate video pipeline. Input: product JSON. Output: ready-to-post draft.**

```
Product JSON
    ↓
AI Image Gen (Freepik)
    ↓
Video Gen (Kling v2)
    ↓
Voiceover (ElevenLabs)
    ↓
Text Overlay
    ↓
TikTok Draft
```

Products supported: TIRTIR, Centella Serum, Medicube (extensible)

---

### 🔍 Apify Universal Scraper
**Run 4,000+ Apify actors directly from your OpenClaw agent.**

```python
# Agent call example
apify_run(actor="apify/instagram-scraper", input={"username": "target"})
```

Covers: TikTok, Instagram, Google Maps, Amazon, and thousands more.

---

### 📊 GoHighLevel MCP
**Full CRM control from your agent — contacts, conversations, pipelines.**

```
Agent reads unresponded leads → drafts replies → updates pipeline stages
```

Production-connected to live GHL location.

---

## Commission a Custom Skill

Have a tool, API, or workflow you want your OpenClaw agent to use?

We scope, build, test, and deliver — with documentation your agent can actually use.

**→ DM [@toniolo32292](https://x.com/toniolo32292) on X**

---

*Toniolo AI Agency · Building agent infrastructure since 2026*
