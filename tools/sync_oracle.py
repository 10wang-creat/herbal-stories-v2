#!/usr/bin/env python3
"""
從本草心語 App（../tcm-oracle-cards-v2/index.html 裡的 `var H=[...]`）同步 81 張卡的精簡資料到
_data/oracle.yml，給網站的 /oracle/ 落地頁、首頁「今日一卡」、文章頁「抽一張卡」使用。

用法：python tools/sync_oracle.py            （App repo 在同一層的 ../tcm-oracle-cards-v2）
      python tools/sync_oracle.py 路徑/index.html
App 的卡片文字改了之後跑一次再 commit 即可。藥材名→卡名的對照表（alias）會保留，不會被覆蓋。
"""
import json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit('請先 pip install pyyaml')

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / '_data' / 'oracle.yml'
src = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / 'tcm-oracle-cards-v2' / 'index.html'
if not src.exists():
    sys.exit(f'找不到 App 的 index.html：{src}')

html = src.read_text(encoding='utf-8', errors='replace')
m = re.search(r'var H=(\[.*?\]);', html, re.S)
if not m:
    sys.exit('index.html 裡找不到 var H=[...]')
cards = json.loads(m.group(1))

old = yaml.safe_load(OUT.read_text(encoding='utf-8')) if OUT.exists() else {}
data = {
    'app_url': old.get('app_url', 'https://tcm-oracle-cards.vercel.app/'),
    'image_base': old.get('image_base', 'https://tcm-oracle-cards.vercel.app/images/'),
    'alias': old.get('alias') or {},
    'cards': [{'id': c['id'], 'n': c['n'], 'cat': c['cat'], 'sub': c.get('sub', ''), 'fn': c.get('fn', ''),
               'mo': c.get('mo', ''), 'af': c.get('af', ''), 'img': c['img']} for c in cards],
}
OUT.write_text('# 由 tools/sync_oracle.py 自動產生（alias 區塊可手動維護）\n' +
               yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=200), encoding='utf-8')
print(f'已同步 {len(cards)} 張卡 → {OUT.relative_to(ROOT)}')
