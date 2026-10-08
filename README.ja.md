# 数学スキルの marketplace

[English](README.md) | 日本語

Yoshito Ishiki が配布する Codex 用プラグインの GitHub marketplace です。
marketplace の識別子は `yoshito-ishiki-math` です。

## 導入

`codex plugin` に対応する Codex CLI で、次を実行します。

```sh
codex plugin marketplace add yoshito-ishiki-math/math-skills-marketplace
codex plugin add math-paper-skills@yoshito-ishiki-math
```

導入後は新しいチャットを開始してください。デスクトップアプリに一覧が
反映されない場合は更新または再起動し、プラグイン一覧で
**Yoshito Ishiki Math** を選んで **Math Paper Skills** をインストールします。

確認コマンドは次のとおりです。

```sh
codex plugin marketplace list
codex plugin list --marketplace yoshito-ishiki-math --json
```

## 収録内容

プラグイン `math-paper-skills` **0.1.0** に、次の3スキルを同梱しています。

| スキル | 用途 |
| --- | --- |
| `write-research-paper` | 所有者の指示に基づく数学論文の執筆・改稿 |
| `read-research-paper` | 明示的に委任された、凍結原稿の独立した文章レビュー |
| `latex-paragraph-ids` | LaTeX 原稿の固定段落 ID と補助ツール |

レビュー用スキルが執筆基準を相対パスで参照するため、3スキルを一緒に
導入する構成です。文章レビューは証明の正しさを保証しません。
個人の原稿やコーパスは含まれていません。任意のコーパス検索ツールには
所有者が指定する入力が必要です。補助スクリプトには Python 3.10 以上を
推奨します。段落 ID の組版には、同梱の利用案内に記載された LaTeX 環境が必要です。

## 更新

```sh
codex plugin marketplace upgrade yoshito-ishiki-math
codex plugin add math-paper-skills@yoshito-ishiki-math
```

配布版は公開コミットから作成したスナップショットです。元リポジトリの
変更は自動反映されません。再現可能な原稿作業では、導入前に版番号と
取得元を確認してください。

## 出典と配布範囲

取得元は [yoshito-ishiki-math/math-paper-skills](https://github.com/yoshito-ishiki-math/math-paper-skills)
のコミット `f2faa773fa073869d29b4e2a369d10170d2a4feb` です。
同リポジトリは [Haruhisa Enomoto の math-paper-skills](https://github.com/haruhisa-enomoto/math-paper-skills)
を基礎としています。元の MIT ライセンスと出典表示を保持しています。

[UPSTREAM.json](UPSTREAM.json) に取得コミット、Git blob の識別子、SHA-256 を記録し、
公開済みの35ファイルを無改変で同梱しています。プラグインの定義とアイコンを追加しました。
この配布構成にはルートの [MIT ライセンス](LICENSE)、取得元のファイルには
[元のライセンス](plugins/math-paper-skills/LICENSE) が適用されます。

これは GitHub リポジトリを登録して使う marketplace です。OpenAI の公式公開
ディレクトリへの申請は行っていません。
[公式の構成案内](https://developers.openai.com/plugins/build/plugins) と
[公開申請の手順](https://developers.openai.com/plugins/deploy/submission) を参照してください。

## 配布構成の検査

```sh
python3 tools/validate.py
python3 -m unittest discover -s plugins/math-paper-skills/tests -v
```

定義・相対パス・スキル間参照・原本との一致・取得元の合成テストを確認します。
数学的検証や、すべての LaTeX 文書クラスでの組版確認ではありません。
