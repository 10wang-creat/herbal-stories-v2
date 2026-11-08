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
