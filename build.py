"""store_assets/プライバシーポリシー.md から GitHub Pages 用の privacy.html と index.html（サポート）を作る。
  python3 build.py  （連絡先は CONTACT に入れる）
"""
import html, re
from pathlib import Path

CONTACT = "〔連絡先メールアドレス〕"
SRC = Path.home() / "Developer/dogasaiseiiPad/store_assets/プライバシーポリシー.md"

STYLE = """
:root{--bg:#f7f7fb;--card:#fff;--text:#1c1c24;--sub:#5b5b6b;--accent:#5a1bd8;--line:#e3e3ec}
@media (prefers-color-scheme:dark){:root{--bg:#121218;--card:#1c1c26;--text:#ececf3;--sub:#a3a3b5;--accent:#b38cff;--line:#2e2e3c}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:16px/1.8 -apple-system,BlinkMacSystemFont,"Hiragino Sans","Hiragino Kaku Gothic ProN",sans-serif}
header{background:linear-gradient(135deg,#101ab4,#9b16fc);color:#fff;padding:36px 16px 28px;text-align:center}
header img{width:84px;height:84px;border-radius:19px;box-shadow:0 6px 20px rgba(0,0,0,.25)}
header h1{margin:12px 0 4px;font-size:24px}header p{margin:0;opacity:.9;font-size:14px;color:#fff}
main{max-width:720px;margin:0 auto;padding:20px 16px 48px}
section{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:4px 20px 12px;margin:16px 0}
h2{font-size:18px;margin:18px 0 6px}h3{font-size:16px;margin:16px 0 4px}
p,li{color:var(--text)}.sub{color:var(--sub);font-size:14px}a{color:var(--accent);word-break:break-all}
nav{text-align:center;margin-top:20px;font-size:14px}nav a{margin:0 10px}
"""

def page(title, body, sub):
    return f"""<!doctype html><html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<link rel="icon" href="icon.png"><style>{STYLE}</style></head><body>
<header><img src="icon.png" alt=""><h1>切り抜き動画プレイヤー</h1><p>{sub}</p></header>
<main>{body}
<nav><a href="index.html">サポート</a><a href="privacy.html">プライバシーポリシー</a></nav>
<p class="sub" style="text-align:center">© 2026 onlinemayuge</p></main></body></html>"""

def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"(https?://[^\s）)]+)", r'<a href="\1">\1</a>', s)

def md_to_html(md):
    out, ul = [], False
    for line in md.splitlines():
        if line.startswith("- "):
            if not ul: out.append("<ul>"); ul = True
            out.append(f"<li>{inline(line[2:])}</li>"); continue
        if ul: out.append("</ul>"); ul = False
        if line.startswith("# "):
            out.append(f"</section><section><h2>{inline(line[2:])}</h2>")
        elif line.startswith("## "):
            out.append(f"<h3>{inline(line[3:])}</h3>")
        elif line.strip() in ("", "---"):
            continue
        else:
            out.append(f"<p>{inline(line)}</p>")
    if ul: out.append("</ul>")
    body = "".join(out)
    return "<section>" + body.removeprefix("</section><section>") + "</section>"

md = SRC.read_text().replace("〔連絡先メールアドレス〕", CONTACT).replace("〔contact email〕", CONTACT)
Path("privacy.html").write_text(page("プライバシーポリシー｜切り抜き動画プレイヤー", md_to_html(md), "プライバシーポリシー / Privacy Policy"))

support = f"""<section><h2>サポート</h2>
<p>「切り抜き動画プレイヤー」は、自分の動画の見たい所だけを切り抜いて、何度でもすぐに見返せる動画プレイヤーです。iPhone・iPad で使えます。</p>
<h3>お問い合わせ</h3><p>不具合のご報告やご質問は、次のアドレスまでお送りください。</p>
<p><strong>{html.escape(CONTACT)}</strong></p>
<p class="sub">お使いの端末（iPhone / iPad の機種）と iOS のバージョン、起きたことを書いていただけると助かります。</p></section>
<section><h2>よくある質問</h2>
<h3>無料版とプロ版のちがいは？</h3><p>無料版は、切り抜きを20件、再生リストを1つまで作れます。プロ版（買い切り980円）にすると、どちらも無制限になります。取り込める動画の数と長さには、どちらも上限がありません。広告はありません。</p>
<h3>機種を変えたら、プロ版を買い直す必要がありますか？</h3><p>いいえ。同じ Apple アカウントなら、設定 → プロ版 → 「購入を復元」で、もう一度使えるようになります。</p>
<h3>動画や切り抜きは、どこに保存されますか？</h3><p>すべてお使いの端末の中です。開発者を含め、外に送られることはありません。アプリを削除すると消えるのでご注意ください。</p>
<h3>ネットの動画をダウンロードできますか？</h3><p>できません。お手元の端末にある動画（自分で撮った動画や、写真・ファイルに入っている動画）を再生・整理するアプリです。</p>
<h3>別の端末に切り抜きを移せますか？</h3><p>動画の「書き出し（他の端末へ共有）」で、動画と切り抜きの情報をまとめて送れます。受け取った端末では、設定の「動画と情報ファイルを読み込む」から、2つのファイルを両方選んでください。</p></section>"""
Path("index.html").write_text(page("サポート｜切り抜き動画プレイヤー", support, "サポート / Support"))
print("ok", "（連絡先未設定）" if "〔" in CONTACT else "")
