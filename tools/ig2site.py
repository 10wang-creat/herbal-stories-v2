# -*- coding: utf-8 -*-
"""
整聊系列：把 IG 文案 + 圖卡轉成網站頁面

讀取「IG中藥整聊」資料夾：
  00/ 裡的四份文案 .md（＋前兩季的圖卡產生器 .html，用來取每張卡的文字）
  01. 陳皮/、02. 龍眼肉/ … 每集的 9 張 PNG（EP*_01.png ~ EP*_09.png）
輸出到網站：
  _zhengliao/<slug>.md                    每集一頁
  _data/zhengliao.yml                     系列總表（入口頁用，未上架的集數也列出來）
  assets/images/zhengliao/<slug>/NN.webp  圖卡（1080px WebP）
  assets/images/og/zl-<slug>.jpg          分享縮圖（第 1 張卡）

用法（在 repo 根目錄）：
  python tools/ig2site.py                       # 用預設路徑 OneDrive\\桌面\\創作素材\\IG中藥整聊
  python tools/ig2site.py "D:\\某處\\IG中藥整聊"   # 指定路徑
新一集的圖卡匯出後，放進「13. 生薑」這類資料夾（編號接續 01–12），再跑一次即可。
已轉過的圖不會重轉；文案改了也是重跑一次。
需要：pip install pillow
"""
import json, os, re, sys, html as htmlmod
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# ---------- 系列與每集的固定資料 ----------
SERIES = [
    dict(key="things", no=1, name="丟不掉的東西", full="丟不掉的東西 × 中醫情志學", emoji="📦",
         sub="衣櫃、書架、抽屜裡，那些捨不得的東西", md="IG貼文文案_丟不掉的東西系列.md",
         gen="herbal-card-generator_丟不掉的東西系列.html", year=2026,
         eps=[("chenpi","陳皮",["陳皮"],"脾"), ("longyanrou","龍眼肉",["龍眼肉"],"腎"),
              ("meigui-bohe","玫瑰薄荷",["薄荷"],"肝"), ("baihe","百合",["百合"],"肺"),
              ("foshou","佛手",["佛手"],"脾"), ("lianzixin","蓮子心",["蓮子心"],"心")]),
    dict(key="habits", no=2, name="戒不掉的習慣", full="戒不掉的習慣 × 中醫情志學", emoji="🔁",
         sub="滑手機、生悶氣、靠咖啡硬撐的那些日常", md="戒不掉的習慣_中醫情志學_IG文案.md",
         gen="herbal-card-generator_戒不掉的習慣系列.html", year=2026,
         eps=[("suanzaoren","酸棗仁",["酸棗仁"],"心"), ("juhua","菊花",["菊花"],"肝"),
              ("fuling","茯苓",["茯苓"],"脾"), ("jiegeng","桔梗",["桔梗"],"肺"),
              ("yuanzhi","遠志",["遠志"],"腎"), ("huangqi","黃耆",["黃耆"],"脾")]),
    dict(key="winter", no=3, name="收不起來的冬天", full="收不起來的冬天 × 節氣整理學", emoji="❄️",
         sub="跟著六個節氣，整理冬天收不起來的東西", md="收不起來的冬天_節氣整理學_IG文案.md",
         gen=None, year=None,
         eps=[("shengjiang","生薑",["生薑"],"脾"), ("rougui","肉桂",["肉桂"],"腎"),
              ("hongzao","紅棗",["大棗","紅棗"],"脾"), ("shanzha","山楂",["山楂"],"脾"),
              ("heizhima","黑芝麻",["黑芝麻"],"腎"), ("gouqi","枸杞",["枸杞子","枸杞"],"肝")]),
    dict(key="people", no=4, name="放不下的人", full="放不下的人 × 中醫情志學", emoji="🤝",
         sub="已讀、群組、通訊錄，和最放不下的自己", md="放不下的人_中醫情志學_IG文案.md",
         gen=None, year=None,
         eps=[("hehuanhua","合歡花",["合歡花","合歡皮"],"心"), ("molihua","茉莉花",["茉莉花"],"肝"),
              ("baiziren","柏子仁",["柏子仁"],"心"), ("gancao","甘草",["甘草"],"脾"),
              ("xiakucao","夏枯草",["夏枯草"],"肝"), ("danggui","當歸",["當歸"],"肝")]),
]
CIRCLED = "①②③④⑤⑥"

# 網站上不需要的 IG 專用句子
DROP_PREFIX = ("這是【", "每集聊", "【", "收藏起來", "整套收藏起來，下次")


def q(s):
    """YAML 字串（JSON 格式的雙引號字串，YAML 可直接讀）"""
    return json.dumps(s, ensure_ascii=False)


def clean_lines(block):
    out = []
    for ln in block.split("\n"):
        t = ln.strip()
        if t.startswith(DROP_PREFIX):
            continue
        out.append(t)
    text = "\n".join(out)
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


# ---------- 前兩季：文案 md（舊格式） ----------
def parse_old_md(path, year):
    s = path.read_text(encoding="utf-8")
    eps = {}
    parts = re.split(r"^## EP(\d)｜", s, flags=re.M)
    for i in range(1, len(parts), 2):
        n = int(parts[i]); body = parts[i + 1]
        head, _, rest = body.partition("\n")
        m = re.match(r"(\d+)/(\d+)（.）・(.+?)\s*×\s*(.+?)(（系列完結）)?\s*$", head.strip())
        mo, d, concept, herb = int(m[1]), int(m[2]), m[3].strip(), m[4].strip()
        rest = re.split(r"^\\?-{3}\s*$|^###", rest, flags=re.M)[0]
        tags = re.findall(r"#[^\s`#]+", " ".join(re.findall(r"`([^`]*#[^`]*)`", rest)))
        rest = re.sub(r"`[^`]*`", "", rest)
        eps[n] = dict(date=f"{year}-{mo:02d}-{d:02d}", concept=concept, paras=clean_lines(rest),
                      hashtags=tags, pinned="", jieqi="")
    return eps


# ---------- 前兩季：從圖卡產生器取 9 張卡的文字 ----------
STR = r'"((?:[^"\\]|\\.)*)"'
def jsstr(x):
    try:
        return json.loads('"' + x + '"')
    except Exception:
        return x.replace('\\"', '"')

def html2text(h):
    h = re.sub(r"<br\s*/?>", "\n", h)
    h = re.sub(r"<[^>]+>", "", h)
    return htmlmod.unescape(h).strip()

def parse_generator(path):
    if not path or not path.exists():
        return {}
    s = path.read_text(encoding="utf-8")
    s = re.sub(r"data:image/[^\"'`)]+", "", s)   # 拿掉內嵌圖片，避免干擾
    ids = [(m.start(), int(m[1])) for m in re.finditer(r'\bid"?\s*:\s*"EP(\d)"', s)]
    out = {}
    for k, (pos, n) in enumerate(ids):
        seg = s[pos: ids[k + 1][0] if k + 1 < len(ids) else len(s)]
        tps = list(re.finditer(r'\btype"?\s*:\s*"(cover|text|knowledge|action|ending)"', seg))
        cards = []
        for j, t in enumerate(tps):
            pg = seg[t.start(): tps[j + 1].start() if j + 1 < len(tps) else len(seg)]
            eb = re.search(r'\beyebrow"?\s*:\s*' + STR, pg)
            hm = re.search(r'\bhtml"?\s*:\s*(?:`([^`]*)`|' + STR + ")", pg)
            lines = []
            if hm:
                lines.append(html2text(hm[1] if hm[1] is not None else jsstr(hm[2])))
            for a in re.finditer(r'\bico"?\s*:\s*' + STR + r'\s*,\s*"?txt"?\s*:\s*' + STR, pg):
                lines.append(f"{jsstr(a[1])} {jsstr(a[2])}")
            tl = re.search(r'\btail"?\s*:\s*(?:`([^`]*)`|' + STR + ")", pg)
            if tl:
                lines.append("→ " + html2text(tl[1] if tl[1] is not None else jsstr(tl[2])))
            cards.append(dict(eyebrow=jsstr(eb[1]) if eb else "", text="\n".join(lines).strip()))
        out[n] = cards[:9]
    return out


# ---------- 後兩季：文案 md（新格式，含逐張圖卡） ----------
def parse_new_md(path):
    s = path.read_text(encoding="utf-8")
    s = s.split("\n# 缺圖藥材")[0]
    eps = {}
    parts = re.split(r"^## EP(\d)｜", s, flags=re.M)
    for i in range(1, len(parts), 2):
        n = int(parts[i]); body = parts[i + 1]
        head, _, rest = body.partition("\n")
        m = re.match(r"(.+?)・(.+?)\s+📅\s*(\d{4})/(\d{2})/(\d{2})", head.strip())
        first, herb = m[1].strip(), m[2].strip()
        date = f"{m[3]}-{m[4]}-{m[5]}"
        sec = dict(re.findall(r"^### (.+?)\n(.*?)(?=^### |\Z)", rest, flags=re.M | re.S))
        cards = []
        for key in sec:
            if key.startswith("圖卡"):
                for cm in re.finditer(r"^\d\.\s*(.*)$", sec[key], flags=re.M):
                    line = cm[1].strip()
                    em = re.match(r"〔(.+?)〕\s*(.*)", line)
                    eyebrow, txt = (em[1], em[2]) if em else ("", line)
                    if "　" in txt and " / " not in txt:
                        lines = [x.strip() for x in txt.split("　") if x.strip()]
                    else:
                        lines = [x.strip() for x in re.split(r"\s/\s?|\s?/\s", " " + txt + " ")]
                        while lines and not lines[0]: lines.pop(0)
                        while lines and not lines[-1]: lines.pop()
                    cards.append(dict(eyebrow=eyebrow, text="\n".join(lines)))
        copy = sec.get("貼文文案", "")
        tags = re.findall(r"#[^\s#]+", "\n".join(l for l in copy.split("\n") if l.strip().startswith("#草本")))
        copy = "\n".join(l for l in copy.split("\n") if not l.strip().startswith("#草本"))
        pinned = sec.get("置頂留言", "").strip().split("\n")[0].strip()
        concept, jieqi = first, ""
        if len(cards) >= 3 and cards[2]["text"]:          # 節氣篇：概念取第 3 張卡的大標
            if re.fullmatch(r"(小雪|大雪|冬至|小寒|大寒|立春)", first):
                jieqi, concept = first, cards[2]["text"].split("\n")[0]
        eps[n] = dict(date=date, concept=concept, jieqi=jieqi, paras=clean_lines(copy),
                      hashtags=tags, pinned=pinned, cards=cards[:9])
    return eps


# ---------- 圖卡 ----------
def find_folder(src, idx):
    for p in src.iterdir():
        m = re.match(r"(\d+)\.?\s*", p.name)
        if p.is_dir() and m and int(m[1]) == idx:
            return p
    return None

def convert_images(folder, slug):
    from PIL import Image
    pngs = sorted(folder.glob("*.png"), key=lambda p: int(re.findall(r"(\d+)\.png$", p.name)[0]))
    if len(pngs) < 9:
        return []
    outdir = REPO / "assets/images/zhengliao" / slug
    outdir.mkdir(parents=True, exist_ok=True)
    urls = []
    for k, p in enumerate(pngs[:9], 1):
        dst = outdir / f"{k:02d}.webp"
        if not dst.exists() or dst.stat().st_mtime < p.stat().st_mtime:
            im = Image.open(p).convert("RGB")
            if im.width > 1080:
                im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
            im.save(dst, "WEBP", quality=82, method=6)
            if k == 1:
                (REPO / "assets/images/og").mkdir(parents=True, exist_ok=True)
                im.save(REPO / f"assets/images/og/zl-{slug}.jpg", "JPEG", quality=85, optimize=True)
        urls.append(f"/assets/images/zhengliao/{slug}/{k:02d}.webp")
    return urls


def md_paras(paras):
    out = []
    for p in paras:
        lines = [l for l in p.split("\n") if l.strip()]
        out.append("  \n".join(lines))         # 行尾兩個空白 = 換行
    return "\n\n".join(out)


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "OneDrive/桌面/創作素材/IG中藥整聊"
    if not src.exists():
        sys.exit(f"找不到資料夾：{src}")
    (REPO / "_zhengliao").mkdir(exist_ok=True)
    data = []
    for S in SERIES:
        mdp = src / "00" / S["md"]
        if S["year"]:
            eps = parse_old_md(mdp, S["year"])
            gcards = parse_generator(src / "00" / S["gen"])
            for n in eps:
                eps[n]["cards"] = gcards.get(n, [])
        else:
            eps = parse_new_md(mdp)
        sd = dict(key=S["key"], no=S["no"], name=S["name"], full=S["full"], emoji=S["emoji"],
                  sub=S["sub"], episodes=[])
        for n, (py, herb, site_herbs, organ) in enumerate(S["eps"], 1):
            e = eps[n]
            slug = f"{S['key']}-{n:02d}-{py}"
            idx = (S["no"] - 1) * 6 + n
            folder = find_folder(src, idx)
            imgs = convert_images(folder, slug) if folder else []
            cards = e.get("cards") or [dict(eyebrow="", text="") for _ in range(9)]
            for k, c in enumerate(cards):
                c["img"] = imgs[k] if k < len(imgs) else ""
            hook = e["paras"][0]
            body = e["paras"][1:]
            title = hook.replace("\n", "")
            excerpt = (body[0] if body else hook).replace("\n", "")
            fm = ["---", "layout: zhengliao",
                  f"title: {q(title)}",
                  f"hook: {q(hook)}",
                  f"date: {e['date']}",
                  f"series_key: {S['key']}", f"series_no: {S['no']}",
                  f"series_name: {q(S['name'])}", f"series_full: {q(S['full'])}",
                  f"ep: {n}", f"ep_mark: {q(CIRCLED[n-1])}",
                  f"herb: {q(herb)}", f"site_herbs: {q(site_herbs)}",
                  f"concept: {q(e['concept'])}", f"organ: {q(organ)}",
                  f"jieqi: {q(e.get('jieqi',''))}",
                  f"excerpt: {q(excerpt)}",
                  f"pinned: {q(e.get('pinned',''))}",
                  f"hashtags: {q(e.get('hashtags', []))}",
                  f"og_image: {q('og/zl-' + slug + '.jpg') if imgs else 'null'}",
                  "cards:"]
            for c in cards:
                fm.append(f"  - {{img: {q(c['img'])}, eyebrow: {q(c['eyebrow'])}, text: {q(c['text'])}}}")
            fm.append("---")
            out = "\n".join(fm) + "\n\n" + md_paras(body) + "\n"
            (REPO / "_zhengliao" / f"{slug}.md").write_text(out, encoding="utf-8")
            sd["episodes"].append(dict(slug=slug, ep=n, date=e["date"], herb=herb, concept=e["concept"],
                                       organ=organ, jieqi=e.get("jieqi", ""), has_img=bool(imgs)))
            print(f"{slug:28s} {e['date']}  {herb:5s} {e['concept']:6s} 圖卡 {'✓' if imgs else '－'}  卡文 {sum(1 for c in cards if c['text'])}/9")
        data.append(sd)
    lines = ["# 由 tools/ig2site.py 自動產生，請勿手改"]
    for sd in data:
        lines.append(f"- key: {sd['key']}")
        for k in ("no", "name", "full", "emoji", "sub"):
            lines.append(f"  {k}: {q(sd[k]) if isinstance(sd[k], str) else sd[k]}")
        lines.append("  episodes:")
        for ep in sd["episodes"]:
            lines.append("    - {" + ", ".join(f"{k}: {q(v) if isinstance(v, str) else str(v).lower()}" for k, v in ep.items()) + "}")
    (REPO / "_data" / "zhengliao.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("完成：_zhengliao/、_data/zhengliao.yml、assets/images/zhengliao/")

if __name__ == "__main__":
    main()
