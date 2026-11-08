#!/usr/bin/env python3
"""
產生文章專屬的社群分享圖（Open Graph image，1200×630 JPG）

用法：
  python tools/make_og.py                 # 幫所有還沒有分享圖的文章產生
  python tools/make_og.py --force         # 全部重新產生（改了版型之後用）
  python tools/make_og.py _stories/si-jun-zi-tang.md   # 只做指定文章

Windows 上直接雙擊「產生分享圖.bat」即可（等同第一個指令）。

輸出到 assets/images/og/<slug>.jpg，<slug> 就是文章檔名（不含 .md）。
_layouts/default.html 會自動偵測這張圖存在就拿來當 og:image，不存在就退回品牌圖。
安裝：pip install pillow pyyaml
"""
import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parent.parent
STORIES = ROOT / '_stories'
CHARS = ROOT / 'assets' / 'images' / 'characters'
LOGO = ROOT / 'assets' / 'images' / 'site-logo.png'
OUT = ROOT / 'assets' / 'images' / 'og'

W, H = 1200, 630
SITE_NAME = '草本故事館'
SITE_URL = 'herbalstoryhouse.com'

# 兩個系列的色票（對應 site.css 的 --green / --fire）
THEMES = {
    'formula': {'a': (59, 86, 76), 'b': (111, 144, 131), 'label': '中藥方劑', 'accent': (198, 204, 214)},
    'paozhi':  {'a': (69, 63, 107), 'b': (137, 129, 194), 'label': '本草炮製', 'accent': (220, 214, 240)},
}

# 字型：依序找得到哪個就用哪個（Linux 的 Noto CJK → Windows 微軟正黑體 → macOS 蘋方）
FONT_CANDIDATES = [
    '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc',
    '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
    '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
    'C:/Windows/Fonts/msjhbd.ttc',
    'C:/Windows/Fonts/msjh.ttc',
    'C:/Windows/Fonts/mingliub.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/STHeiti Medium.ttc',
]


def find_font():
    for f in FONT_CANDIDATES:
        if Path(f).exists():
            return f
    sys.exit('找不到中文字型，請在 tools/make_og.py 的 FONT_CANDIDATES 加上你電腦的字型路徑。')


FONT_PATH = find_font()
# .ttc 內含多個字型；Noto Serif CJK 的 TC 在 index 2（SC=0, JP=1? 依版本不同），找不到就退回 0
def load_font(size):
    for idx in (2, 0):
        try:
            return ImageFont.truetype(FONT_PATH, size, index=idx)
        except OSError:
            continue
    return ImageFont.truetype(FONT_PATH, size)


def read_front_matter(path: Path) -> dict:
    text = path.read_text(encoding='utf-8')
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, flags=re.S)
    if not m:
        return {}
    if yaml:
        return yaml.safe_load(m.group(1)) or {}
    # 沒有 PyYAML 時的簡易解析（只抓需要的欄位）
    fm = {}
    for key in ('title', 'formula', 'series'):
        mm = re.search(rf'^{key}:\s*"?(.+?)"?\s*$', m.group(1), flags=re.M)
        if mm:
            fm[key] = mm.group(1)
    fm['ingredients'] = [{'image': i} for i in re.findall(r'^\s+image:\s*(\S+)', m.group(1), flags=re.M)]
    return fm


def gradient(w, h, c1, c2):
    """左上 c1 → 右下 c2 的斜向漸層。"""
    base = Image.new('RGB', (w, h), c1)
    top = Image.new('RGB', (w, h), c2)
    small_w, small_h = 120, 63  # 先算小圖再放大，省時間
    data = bytes(int(255 * (0.62 * x / (small_w - 1) + 0.38 * y / (small_h - 1)))
                 for y in range(small_h) for x in range(small_w))
    mask = Image.frombytes('L', (small_w, small_h), data).resize((w, h), Image.BICUBIC)
    return Image.composite(top, base, mask)


def wrap_text(draw, text, font, max_width):
    """中文逐字換行（英文字母／數字不拆字）。"""
    lines, cur = [], ''
    tokens = re.findall(r'[A-Za-z0-9]+|.', text)
    for tok in tokens:
        test = cur + tok
        if draw.textlength(test, font=font) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = tok
    if cur:
        lines.append(cur)
    return lines


def fit_title(draw, text, max_width, max_lines=3, start=64, floor=40):
    """自動縮字直到塞得進 max_lines 行。"""
    size = start
    while size >= floor:
        font = load_font(size)
        lines = wrap_text(draw, text, font, max_width)
        if len(lines) <= max_lines:
            return font, lines
        size -= 4
    font = load_font(floor)
    lines = wrap_text(draw, text, font, max_width)[:max_lines]
    lines[-1] = lines[-1][:-1] + '…'
    return font, lines


def paste_character(canvas, img_path: Path, box, shadow=True):
    try:
        im = Image.open(img_path).convert('RGBA')
    except OSError:
        return
    im.thumbnail((box[2], box[3]), Image.LANCZOS)
    x = box[0] + (box[2] - im.width) // 2
    y = box[1] + (box[3] - im.height) // 2
    if shadow:
        sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
        alpha = im.split()[3].point(lambda a: int(a * 0.35))
        sh.putalpha(alpha)
        sh = sh.filter(ImageFilter.GaussianBlur(14))
        canvas.alpha_composite(sh, (x + 6, y + 14))
    canvas.alpha_composite(im, (x, y))


def make_one(story: Path, force=False) -> bool:
    fm = read_front_matter(story)
    title = str(fm.get('title', story.stem)).strip()
    formula = str(fm.get('formula', '') or '').strip()
    series = 'paozhi' if fm.get('series') else 'formula'
    theme = THEMES[series]
    out = OUT / f'{story.stem}.jpg'
    if out.exists() and not force:
        return False

    canvas = gradient(W, H, theme['a'], theme['b']).convert('RGBA')
    # 淡淡的裝飾圓，讓背景不會太平
    deco = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(deco).ellipse((820, -260, 1420, 340), fill=(255, 255, 255, 18))
    ImageDraw.Draw(deco).ellipse((-180, 380, 420, 980), fill=(255, 255, 255, 14))
    canvas.alpha_composite(deco)
    draw = ImageDraw.Draw(canvas)

    # 右側角色圖（最多 3 張）
    images = [i.get('image') for i in (fm.get('ingredients') or []) if isinstance(i, dict) and i.get('image')]
    images = [CHARS / i for i in images if (CHARS / i).exists()][:3]
    text_right = W - 60  # 文字區右界
    if images:
        text_right = 700
        n = len(images)
        if n == 1:
            paste_character(canvas, images[0], (720, 95, 420, 440))
        elif n == 2:
            paste_character(canvas, images[0], (720, 70, 300, 300))
            paste_character(canvas, images[1], (880, 270, 290, 290))
        else:
            paste_character(canvas, images[0], (740, 50, 270, 270))
            paste_character(canvas, images[1], (930, 150, 240, 240))
            paste_character(canvas, images[2], (760, 330, 260, 260))

    # 左側文字
    x0 = 64
    # 系列小標
    badge_font = load_font(26)
    badge = f'{theme["label"]}'
    bw = draw.textlength(badge, font=badge_font) + 36
    pill = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle((x0, 60, x0 + bw, 60 + 48), radius=24, fill=(255, 255, 255, 56))
    canvas.alpha_composite(pill)
    draw = ImageDraw.Draw(canvas)
    draw.text((x0 + 18, 60 + 8), badge, font=badge_font, fill=(255, 255, 255, 255))

    # 標題
    title_font, lines = fit_title(draw, title, text_right - x0, max_lines=3)
    y = 140
    line_h = int(title_font.size * 1.3)
    for ln in lines:
        draw.text((x0 + 3, y + 3), ln, font=title_font, fill=(0, 0, 0, 70))
        draw.text((x0, y), ln, font=title_font, fill=(255, 255, 255, 255))
        y += line_h

    # 方劑名
    if formula and formula not in title:
        f_font = load_font(34)
        draw.text((x0, y + 10), formula,
                  font=f_font, fill=theme['accent'] + (255,))

    # 底部：logo + 站名 + 網址
    bar_y = H - 96
    draw.line((x0, bar_y, text_right, bar_y), fill=(255, 255, 255, 60), width=2)
    try:
        logo = Image.open(LOGO).convert('RGBA').resize((56, 56), Image.LANCZOS)
        canvas.alpha_composite(logo, (x0, bar_y + 20))
        lx = x0 + 70
    except OSError:
        lx = x0
    name_font = load_font(30)
    url_font = load_font(22)
    draw.text((lx, bar_y + 18), SITE_NAME, font=name_font, fill=(255, 255, 255, 255))
    draw.text((lx, bar_y + 56), SITE_URL, font=url_font, fill=(255, 255, 255, 190))

    OUT.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(out, 'JPEG', quality=86, optimize=True, progressive=True)
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('stories', nargs='*', help='指定文章（預設：_stories 全部）')
    ap.add_argument('--force', action='store_true', help='已存在也重新產生')
    args = ap.parse_args()

    targets = [Path(s) for s in args.stories] if args.stories else sorted(STORIES.glob('*.md'))
    made = skipped = 0
    for st in targets:
        if make_one(st, force=args.force):
            made += 1
            print(f'✓ {st.stem}.jpg')
        else:
            skipped += 1
    print(f'\n完成：新產生 {made} 張，略過 {skipped} 張（已存在）。輸出：{OUT.relative_to(ROOT)}/')


if __name__ == '__main__':
    main()
