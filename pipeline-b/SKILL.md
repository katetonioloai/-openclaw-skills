---
name: pipeline-b
description: Run the Pipeline B TikTok Shop BOF (bottom-of-funnel) video generator for Toniolo AI Agency. Use when asked to generate, run, submit, or collect BOF videos for TikTok affiliate products (TIRTIR, Centella Serum, Medicube, or any product JSON). Also use when checking Pipeline B status, troubleshooting video generation errors, or managing the products queue.
---

# Pipeline B — TikTok BOF Video Generator

Generates 9-second affiliate videos: Before image → Product demo → After image, with ElevenLabs voiceover.

## Location
```
/Users/tonioloai/.openclaw/workspace/pipeline-b/
```
**Always activate venv before running:**
```bash
cd /Users/tonioloai/.openclaw/workspace/pipeline-b
source venv/bin/activate
```

## API Keys
Load from `~/.secrets/agents.env` — **never source the whole file** (RSA key breaks it):
```bash
export FREEPIK_API_KEY=$(grep FREEPIK_API_KEY ~/.secrets/agents.env | cut -d= -f2)
export ELEVENLABS_API_KEY=$(grep ELEVENLABS_API_KEY ~/.secrets/agents.env | cut -d= -f2)
```

## Run Modes

### Sync (blocking, ~7-10 min)
```bash
python generate_video.py product.json
```
Waits for full pipeline to complete. Use for single one-off videos.

### Async (recommended for queues)
```bash
# Step 1: Submit jobs (exits fast, ~30 sec)
python generate_video.py product.json --async

# Step 2: Collect results when ready (run 3-5 min later)
python generate_video.py --collect
```
⚠️ **Freepik URLs expire in 2-3 hours** — run `--collect` within that window or you'll get 403s. The script auto-re-fetches fresh URLs on 403.

## Products Queue
Current queue lives at `products_queue.json`. Products: TIRTIR Red Cushion, Centella Serum, Medicube Vita C Pads.

To run the whole queue:
```bash
for f in tirtir_product.json centella_product.json medicube_product.json; do
  python generate_video.py $f --async
  sleep 10
done
# Then collect after ~5 min:
python generate_video.py --collect
```

## Output
- Final MP4: `output/bof_{product}_{timestamp}.mp4`
- Temp files: `tmp/` (before/after images, voiceover, demo video)
- Pending jobs state: `tmp/pending_jobs.json`

## Product JSON Format
```json
{
  "product_name": "TIRTIR Red Cushion Foundation",
  "price": "29.99",
  "original_price": "39.99",
  "discount_code": "GLOW20",
  "commission": "18%"
}
```

## BOF Script Formula
Hook → Orange cart CTA → Discount code → Urgency ("ends TONIGHT")
Generated automatically from product JSON. No manual writing needed.

## Video Stack
- **Freepik Mystic** — AI influencer before/after images
- **Freepik Kling v2** — Image-to-video animation
- **ElevenLabs** — Voiceover (Sarah voice, `eleven_turbo_v2`)
- **FFmpeg** — Final 1080x1920 assembly (3 segments × 4s = 12s total)

## Advanced: UGC Variants

### Sync.so Lip Sync (HeyGen avatar + ElevenLabs audio)
```bash
python synclip_ugc.py --video avatar.mp4 --audio voice.wav --output final.mp4
# Pro quality: add --model lipsync-2-pro (~$0.08/sec)
```

### SadTalker Local (talking head, FREE, runs on Mac mini)
```bash
python sadtalker_ugc.py --image face.png --audio voice.mp3 --output video.mp4 --enhancer gfpgan
# Still mode for AI faces: add --still
# Higher res: add --size 512
```
SadTalker conda env: `sadtalker` (Python 3.8). ~15-30 min for 30sec audio on CPU.

## Common Errors
- **403 on Kling video download** → run `--collect` again (script auto re-fetches URL)
- **Image returns no URL** → wait 30s more, re-run `--collect` (COMPLETED but URL not ready yet)
- **FFmpeg drawtext missing** → text overlay uses Pillow instead (already handled in code)
- **venv missing** → `pip3 install -r requirements.txt` in the pipeline-b dir

## References
- See `references/product-prompts.md` for before/after image prompt templates
- See `references/bof-formula.md` for the full BOF script and video formula
