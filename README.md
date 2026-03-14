# OpenClaw Skills — Toniolo AI Agency

Custom skills built for the [OpenClaw](https://github.com/openclaw/openclaw) agent platform.

## What is an OpenClaw Skill?

A skill is a packaged capability that any OpenClaw agent can use. Drop it in your workspace, and your agent instantly gains new tools — no setup beyond the skill folder itself.

## Skills in this repo

### 🎬 tiktok-text-overlay
Add branded text overlays to TikTok videos for Shop/BOF content.
- **PILL style** — Two stacked deal announcement boxes (red + white)
- **HOOK style** — Large screen-filling hook text (@cakedfinds style)
- Fully automated via `ffmpeg` + Python
- Used in production for TikTok Shop affiliate campaigns

**Usage:**
```bash
python3 tiktok-text-overlay/scripts/overlay.py \
  --style hook \
  -i input.mp4 \
  -o output.mp4 \
  --text "Someone fcked up at TikTok cus today the TIRTIR Foundation is on a triple discount..."
```

---

## About

Built by [Toniolo AI Agency](https://x.com/toniolo32292).  
We design and build custom OpenClaw skills for your agent stack.  
→ DM on X to commission a skill.
