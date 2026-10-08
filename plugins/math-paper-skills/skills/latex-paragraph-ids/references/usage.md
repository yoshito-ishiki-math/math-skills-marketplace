# paragraphids v0.4

showkeysから独立した、段落の固定ランダムIDです。v0.1のauto連動は廃止しました。

```tex
\usepackage{paragraphids} % 表示。通常の非表示は [hide]
...
\paraid{p-a7f3c921e40b}
Paragraph text.
```

IDは段落冒頭の独立した一行に置き、本文との間に空行を入れません。
定理・証明の開始や `\item` はIDより前の別行に置きます。
新規段落には新ID、修正・移動では既存IDを保持します。分割時は一方に元IDを残します。

提出・公開用コピーでは、次のように両方をコメントアウトします。

```tex
% \usepackage{paragraphids}
...
% \paraid{p-a7f3c921e40b}
Paragraph text.
```

パッケージ固有の表示切替・書体・幅の設定もコメントアウトします。
showkeysを使用していれば、その読み込みもコメントアウトします。
提出物にはparagraphids.styは不要です。提出ファイルだけを別フォルダへ展開して
コンパイルし、本文の改行・改ページと非表示を確認します。コメントのIDはソースに残ります。

## 共通skillからの導入

`python3 <skill>/scripts/install.py <main-tex-directory>` でパッケージをコピーします。
既存の異なる版は上書きせず停止します。v0.1からの更新では `[auto]` を外し、
showkeysの有無に頼っていた表示設定を明示的な `[hide]` などへ変更します。

```sh
python3 <skill>/scripts/paraids.py new --root /path/to/paper --count 3
python3 <skill>/scripts/paraids.py find p-a7f3c921e40b --root /path/to/paper
python3 <skill>/scripts/paraids.py check --root /path/to/paper
```

同梱版では `<skill>/scripts/paraids.py` の代わりに `paraids.py` を使用できます。
補助ツールはPython 3.9以上、追加ライブラリ不要で、原稿を書き換えません。
IDはp-とランダムな16進12桁。生成時に検索範囲内の既存IDとの重複を避けます。
走査対象はUTF-8の明示的なタグです。新ID発行ではコメント内のIDも予約済みとして扱います。
検索・検査では `--include-comments` を指定するとコメント内も対象にできます。
削除済みの履歴は走査しないため、廃止IDを再利用しないための記録は残します。TeXの条件分岐やマクロ展開は評価しません。
別版を含まない検索範囲を指定してください。TeX側も有効なタグの形式と重複を検査します。

LaTeX 2020-10-01以降とmarginnoteを使用します。位置確定には2回コンパイルします。
片面・両面、奇数・偶数ページとも物理的な左余白に表示します。
二段組でも両方の段のIDをページ左余白に出すため、同じ高さのIDは重なる可能性があります。狭い余白や他の注との
衝突回避は行いません。文書クラスごとの配置確認が必要です。

通常作業用の切替は `[show]` / `[hide]` または `\ParagraphIDsOn` / `\ParagraphIDsOff`。
`\paragraphidfont` と `\paragraphidwidth` で書体と幅を調整できます。
既にmarginnoteを別オプションで使う原稿ではオプション競合にも注意してください。

## 編集と提出の追加規則

- ID行は本文と一緒に移動し、単独で移動しません。コピー先は新IDにします。
- IDと対応する本文の間に見出しや別段落を挟みません。
- 提出処理の再実行では既存コメントを変更せず、%を重ねません。本文と段落区切りを保持します。
- 提出用コピーを使える場合は作業版の表示設定を保持します。
- ID・キーの非表示と、本文内容・改行・改ページの維持は別々に確認し、既存の提出検査にまとめます。

## 赤字の指摘注記（v0.4）

```tex
\paraid{p-a7f3c921e40b}
\paranote{1}{この段落は前の説明と重複。短縮を検討。}
Paragraph text.
```

番号は手動指定です。左余白に赤字で折り返して表示します。
`\paranote[15pt]{2}{指摘内容}` の任意引数で上下位置を調整できます。
標準位置は8pt下、幅は25mm、文字は8ptです。`[hide]` でIDと注記をともに隠します。
幅は `\setlength\paragraphnotewidth{25mm}`、書体は `\paragraphnotefont` で調整できます。
自動衝突回避はありません。長い注記や近接した注記はPDFで重なり・はみ出しを確認してください。
日本語は原稿側の日本語対応エンジン・フォントが必要です。

注記は元の原稿に記入して構いません。提出・公開用では、全paranote行（複数行なら全行）と
専用設定を必ずコメントアウトします。パッケージ読み込みとparaidも従来どおりコメントアウトし、
最終PDFに赤字指摘が一切ないことを確認します。本文と注記を同じソース行に置かないでください。
