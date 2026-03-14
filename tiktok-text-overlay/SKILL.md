---
name: tiktok-text-overlay
description: Add text overlays to TikTok videos. Two styles — PILL (BOF deal boxes) and HOOK (big screen text). Used by Kate and Lexie for TikTok Shop BOF content.
metadata:
  openclaw:
    emoji: "🎬"
    requires:
      bins: ["ffmpeg", "ffprobe", "python3"]
---

# TikTok Text Overlay Skill

Add text-on-screen overlays to TikTok videos for BOF (bottom-of-funnel) content.

## ⚠️ Rules
- **NO EMOJIS in overlay text** — they render as black squares on TikTok. Plain text only.

## Two Styles

### PILL — Deal Announcement Boxes
Two stacked rounded pill boxes centered on screen.
- Top pill: Red (#D63031), white text (e.g. "DOUBLE DISCOUNT")
- Bottom pill: White, black text (e.g. "FINAL HOURS")
- Font: Arial Black
- Use for: product deal announcements, urgency CTAs

### HOOK — Big Screen Text
Large white text with black outline filling the top half of the screen.
- Font: Arial Rounded Bold ✅ (Patricia-approved 2026-03-13, replaced Baskerville)
- White fill, black stroke outline
- Centered, wraps across multiple lines
- Use for: hook text, storytelling openers, @cakedfinds style

## Usage

```bash
# PILL style (default text)
python3 {baseDir}/scripts/overlay.py --style pill -i input.mp4 -o output.mp4

# PILL style (custom text)
python3 {baseDir}/scripts/overlay.py --style pill -i input.mp4 -o output.mp4 --top "FLASH SALE" --bottom "ENDS TONIGHT"

# HOOK style
python3 {baseDir}/scripts/overlay.py --style hook -i input.mp4 -o output.mp4 --text "Someone fcked up at TikTok cus today the EUHOMY Ice Maker is on a triple discount with free shipping..."

# Optional: trim first N seconds
python3 {baseDir}/scripts/overlay.py --style pill -i input.mp4 -o output.mp4 --trim 2
```

## Hook Text Templates
Swap [PRODUCT] with the actual product name:
- "Someone fcked up at TikTok cus today the [PRODUCT] is on a triple discount with free shipping..."
- "Someone fcked up at TikTok cus today the [PRODUCT] is on a triple discount with free shipping... 😳"
- "Condolences to the girlies who got the [PRODUCT] cus it just went on a massive sale with free shipping 😳"

## Pill Text Variations
See `references/pill_hooks.md` for all 14 approved top/bottom combos.
