"""
TikTok Text Overlay — Two Styles
  PILL: Stacked rounded pill boxes (DOUBLE DISCOUNT / FINAL HOURS)
  HOOK: Large white text with black outline (@cakedfinds style)

Usage:
  python3 overlay.py --style pill -i input.mp4 -o output.mp4 [--top "TEXT"] [--bottom "TEXT"] [--trim 2]
  python3 overlay.py --style hook -i input.mp4 -o output.mp4 --text "Hook text here" [--trim 0]
"""

import argparse
import json
import subprocess
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

# ── Font paths (macOS) ──
ARIAL_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
ARIAL_ROUNDED_BOLD = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
BASKERVILLE_TTC = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
BASKERVILLE_SEMIBOLD_INDEX = 4

# ── Active hook font (change this to swap fonts) ──
HOOK_FONT_PATH = ARIAL_ROUNDED_BOLD
HOOK_FONT_INDEX = None  # None for .ttf, int for .ttc


def get_video_dimensions(path):
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", path],
        capture_output=True, text=True
    )
    streams = json.loads(result.stdout)["streams"]
    vs = next(s for s in streams if s["codec_type"] == "video")
    return int(vs["width"]), int(vs["height"])


def create_pill_overlay(w, h, top_text="DOUBLE DISCOUNT", bottom_text="FINAL HOURS"):
    """Style PILL — two stacked rounded pill boxes, centered."""
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Scale boxes relative to video width
    scale = w / 480
    box1_w = int(410 * scale)
    box1_h = int(66 * scale)
    box2_w = int(340 * scale)
    box2_h = int(58 * scale)
    total_h = box1_h + box2_h
    radius = int(14 * scale)

    box1_x = (w - box1_w) // 2
    box1_y = (h - total_h) // 2
    box2_x = (w - box2_w) // 2
    box2_y = box1_y + box1_h  # touching, no gap

    # Draw boxes
    draw.rounded_rectangle([box1_x, box1_y, box1_x + box1_w, box1_y + box1_h],
                           radius=radius, fill="#D63031")
    draw.rounded_rectangle([box2_x, box2_y, box2_x + box2_w, box2_y + box2_h],
                           radius=radius, fill="white")

    # Fonts (scale with video)
    font_large = ImageFont.truetype(ARIAL_BLACK, int(36 * scale))
    font_small = ImageFont.truetype(ARIAL_BLACK, int(32 * scale))

    # Top text (white on red)
    bb = draw.textbbox((0, 0), top_text, font=font_large)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    draw.text(
        (box1_x + (box1_w - tw) // 2 - bb[0], box1_y + (box1_h - th) // 2 - bb[1]),
        top_text, font=font_large, fill="white"
    )

    # Bottom text (black on white)
    bb2 = draw.textbbox((0, 0), bottom_text, font=font_small)
    tw2, th2 = bb2[2] - bb2[0], bb2[3] - bb2[1]
    draw.text(
        (box2_x + (box2_w - tw2) // 2 - bb2[0], box2_y + (box2_h - th2) // 2 - bb2[1]),
        bottom_text, font=font_small, fill="black"
    )

    return overlay


def create_hook_overlay(w, h, text=""):
    """Style HOOK — large white text, black outline, top half of screen."""
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Font size scales with video width, target ~48px at 1080w
    font_size = max(int(w * 0.08), 28)
    stroke_w = max(int(font_size * 0.07), 2)
    if HOOK_FONT_INDEX is not None:
        font = ImageFont.truetype(HOOK_FONT_PATH, font_size, index=HOOK_FONT_INDEX)
    else:
        font = ImageFont.truetype(HOOK_FONT_PATH, font_size)

    # Word-wrap to ~20 chars per line (adjust for width)
    chars_per_line = max(int(w / (font_size * 0.55)), 15)
    # Strip text and filter empty lines to avoid trailing blank/square
    text = text.strip()
    lines = [l for l in textwrap.wrap(text, width=chars_per_line) if l.strip()]
    block = "\n".join(lines)

    # Measure total text block
    bb = draw.multiline_textbbox((0, 0), block, font=font)
    text_h = bb[3] - bb[1]

    # Center horizontally, place in top 40% of frame
    x = w // 2
    y = int(h * 0.50)  # vertically centered

    draw.multiline_text(
        (x, y), block, font=font,
        fill="white", stroke_width=stroke_w, stroke_fill="black",
        anchor="ma", align="center"
    )

    return overlay


def render_video(input_path, output_path, overlay_img, trim_seconds=0):
    overlay_path = "/tmp/tiktok_overlay_tmp.png"
    overlay_img.save(overlay_path)

    cmd = ["ffmpeg", "-y"]
    if trim_seconds > 0:
        cmd += ["-ss", str(trim_seconds)]
    cmd += [
        "-i", input_path,
        "-i", overlay_path,
        "-filter_complex", "[0:v][1:v]overlay=0:0:format=auto",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac",
        output_path,
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Done: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="TikTok text overlay — PILL or HOOK style")
    parser.add_argument("--style", required=True, choices=["pill", "hook"], help="Overlay style")
    parser.add_argument("-i", "--input", required=True, help="Input video path")
    parser.add_argument("-o", "--output", required=True, help="Output video path")
    parser.add_argument("--top", default="DOUBLE DISCOUNT", help="PILL: top box text")
    parser.add_argument("--bottom", default="FINAL HOURS", help="PILL: bottom box text")
    parser.add_argument("--text", default="", help="HOOK: full screen text")
    parser.add_argument("--trim", type=int, default=0, help="Trim N seconds from start")
    args = parser.parse_args()

    w, h = get_video_dimensions(args.input)
    print(f"Video: {w}x{h}")

    if args.style == "pill":
        overlay = create_pill_overlay(w, h, args.top, args.bottom)
    else:
        if not args.text:
            print("ERROR: --text is required for hook style")
            sys.exit(1)
        overlay = create_hook_overlay(w, h, args.text)

    render_video(args.input, args.output, overlay, args.trim)


if __name__ == "__main__":
    main()
