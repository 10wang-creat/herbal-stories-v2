# tools：圖片轉 WebP（可去背）

網站上的角色圖統一規格：長邊 1024px、WebP 品質 85、保留透明。
新圖片請先用這裡的工具處理，再放進 `assets/images/characters/`。

## 第一次使用（Windows）
在 repo 根目錄開 PowerShell 或 cmd：
```
pip install pillow
pip install "rembg[cpu]"      # 需要去背功能才裝；第一次去背會自動下載約 170MB 模型
```

## 平常怎麼用
- 把圖片（或整個資料夾）拖到 `轉WebP.bat` → 旁邊會多出 `webp/` 資料夾，裡面是轉好的檔。
- 要去背就拖到 `去背+轉WebP.bat`。
- 把 `webp/` 裡的檔案搬到 `assets/images/characters/`，在故事的 front matter 寫 `image: 檔名.webp`。

## 命令列
```
python tools/img2webp.py 圖片或資料夾...
python tools/img2webp.py --rembg 圖片...
python tools/img2webp.py --out assets/images/characters 圖片...   # 直接輸出到網站資料夾
python tools/img2webp.py --size 800 --quality 80 圖片...
```

## 去背注意
- 預設模型 u2net 對目前這種「貼紙卡片」風格最乾淨。若角色邊緣被吃掉，試 `--model isnet-anime`。
- 原本就有透明背景的 PNG 不需要去背，直接用 `轉WebP.bat` 即可。
- 去背會順便裁掉四周多餘的透明區域。

---

# tools：文章分享圖（og:image）

每篇文章在 FB／LINE／IG 分享時顯示的縮圖，由 `make_og.py` 自動產生：
深色系列漸層底 + 文章標題 + 方劑名 + 前三位角色圖，1200×630 JPG，輸出到 `assets/images/og/<文章檔名>.jpg`。
`_layouts/default.html` 會自動偵測：有這張圖就用它，沒有就退回品牌圖 `og-image.png`。

## 平常怎麼用
- 寫完新文章、放好角色圖後，雙擊 `產生分享圖.bat`（只會幫還沒有圖的文章產生），再一起 commit。
- 改了標題或角色圖想重做：`python tools/make_og.py --force _stories/檔名.md`
- 改了版型想全部重做：`python tools/make_og.py --force`

## 注意
- 字型會依序找 Noto CJK → 微軟正黑體（Windows）→ 蘋方（macOS）；都找不到會提示你在 `FONT_CANDIDATES` 加路徑。
- 需要 `pip install pillow pyyaml`。
- FB 分享圖有快取：圖換了但 FB 還顯示舊圖時，到 https://developers.facebook.com/tools/debug/ 貼網址按「重新抓取」。

---

# tools：同步本草心語卡片資料

網站的 `/oracle/` 落地頁、首頁「今日一卡」、每篇文章結尾的「抽一張卡」都讀 `_data/oracle.yml`。
這個檔由 `sync_oracle.py` 從 App repo（`../tcm-oracle-cards-v2/index.html` 裡的 `var H=[...]`）抓出來：

```
python tools/sync_oracle.py
```

- App 的卡片文字或圖片檔名有改，跑一次再 commit 網站即可。
- `alias:` 區塊是「文章裡的藥材名 → 卡名」對照（炙甘草→甘草、麥冬→麥門冬…），手動維護，同步時不會被覆蓋。
- 卡圖直接連 `https://tcm-oracle-cards.vercel.app/images/<img>.webp`，網站 repo 不另存一份。

---

# tools：整聊系列（IG 圖卡 → 網站）

`/zhengliao/` 總覽頁和每集頁面，由 `ig2site.py` 從「IG中藥整聊」資料夾產生：
文案讀 `00/` 裡的四份 .md（前兩季的逐張卡片文字從圖卡產生器 .html 取），圖卡讀 `01. 陳皮/`～`12. 黃耆/` 這類編號資料夾。

## 平常怎麼用
1. 新一集的 9 張圖卡匯出後，照編號放進新資料夾：13 生薑、14 肉桂 … 24 當歸（例：`13. 生薑`）。
2. 在 repo 根目錄跑：`python tools/ig2site.py`
   （路徑不是預設的 `OneDrive\桌面\創作素材\IG中藥整聊` 時，在後面加上資料夾路徑）
3. commit。頁面日期就是 IG 發布日，每天早上 8 點的自動重建會讓它當天上線。

## 說明
- 還沒放圖卡的集數，網站會用米色紙卡顯示該集的卡片文字，之後補圖再跑一次就會換成圖。
- 文案 .md 改了也是重跑一次；已轉過、沒變動的圖不會重轉。
- 輸出：`_zhengliao/*.md`、`_data/zhengliao.yml`、`assets/images/zhengliao/`、`assets/images/og/zl-*.jpg`。這些都是自動產生的，要改內容請改 IG 文案 .md。
- 新系列：在 `ig2site.py` 最上面的 `SERIES` 加一段（系列名、文案檔名、每集的拼音與藥材）。
- 需要：`pip install pillow`
