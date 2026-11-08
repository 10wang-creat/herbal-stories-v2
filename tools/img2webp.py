#!/usr/bin/env python3
"""
圖片 → WebP 轉換工具（可選去背）

用法：
  python img2webp.py 圖片或資料夾 [更多圖片或資料夾...]
  python img2webp.py --rembg 圖片或資料夾        # 先去背再轉
  python img2webp.py --out 輸出資料夾 圖片...      # 指定輸出位置

Windows 上直接把圖片或資料夾拖到「轉WebP.bat」或「去背+轉WebP.bat」即可。

預設：長邊縮到 1024px、WebP 品質 85、保留透明度，輸出到來源旁邊的 webp/ 子資料夾。
安裝：pip install pillow            （去背另需 pip install "rembg[cpu]"，第一次執行會下載約 170MB 模型）
"""
import argparse
import sys
from pathlib import Path

from PIL import Image

EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tif', '.tiff'}


def collect(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for f in sorted(p.iterdir()):
                if f.suffix.lower() in EXTS and not f.name.startswith('.'):
                    yield f
        elif p.suffix.lower() in EXTS:
            yield p


def process(src: Path, out_dir: Path, max_side: int, quality: int, remove_bg: bool, session):
    im = Image.open(src)
    if remove_bg:
        from rembg import remove
        im = remove(im, session=session)  # 回傳 RGBA
    elif im.mode not in ('RGB', 'RGBA'):
        im = im.convert('RGBA')

    w, h = im.size
    scale = max_side / max(w, h)
    if scale < 1:
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)

    # 去背後裁掉四周多餘透明區域，再留一點邊
    if remove_bg and im.mode == 'RGBA':
        bbox = im.getbbox()
        if bbox:
            pad = round(max(im.size) * 0.03)
            l, t, r, b = bbox
            im = im.crop((max(0, l - pad), max(0, t - pad), min(im.width, r + pad), min(im.height, b + pad)))

    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / (src.stem + '.webp')
    im.save(dst, 'WEBP', quality=quality, method=6)
    return dst


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('paths', nargs='+', help='圖片檔或資料夾')
    ap.add_argument('--rembg', action='store_true', help='先用 rembg 去背')
    ap.add_argument('--out', help='輸出資料夾（預設：來源旁邊的 webp/）')
    ap.add_argument('--model', default='u2net',
                    help='去背模型（預設 u2net，對貼紙卡片風格最乾淨；可試 isnet-general-use、isnet-anime）')
    ap.add_argument('--size', type=int, default=1024, help='長邊像素上限（預設 1024）')
    ap.add_argument('--quality', type=int, default=85, help='WebP 品質 1-100（預設 85）')
    args = ap.parse_args()

    files = list(collect(args.paths))
    if not files:
        print('找不到可處理的圖片。支援：' + ' '.join(sorted(EXTS)))
        sys.exit(1)

    session = None
    if args.rembg:
        try:
            from rembg import new_session
        except ImportError:
            print('缺少 rembg，請先執行：pip install "rembg[cpu]"')
            sys.exit(1)
        print('載入去背模型（第一次會下載約 170MB）...')
        session = new_session(args.model)

    before = after = 0
    for f in files:
        out_dir = Path(args.out) if args.out else f.parent / 'webp'
        try:
            dst = process(f, out_dir, args.size, args.quality, args.rembg, session)
        except Exception as e:  # noqa: BLE001
            print(f'[失敗] {f.name}: {e}')
            continue
        b, a = f.stat().st_size, dst.stat().st_size
        before += b
        after += a
        print(f'{f.name:40s} {b/1024/1024:6.1f} MB → {a/1024:6.0f} KB   {dst}')

    if before:
        print(f'\n完成 {len(files)} 張：{before/1024/1024:.0f} MB → {after/1024/1024:.1f} MB（剩 {after/before*100:.1f}%）')


if __name__ == '__main__':
    main()
