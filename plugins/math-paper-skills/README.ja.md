# 数学論文の執筆・レビュー用skills

[English](README.md) | 日本語

[Haruhisa Enomoto氏の math-paper-skills](https://github.com/haruhisa-enomoto/math-paper-skills) を元にした公開フォークです。元のMITライセンスと著作権表示を保持し、追加した執筆・レビュー手順から汎用部分を収録しています。個人の研究記録、著者を特定するプロファイル情報、論文コーパス、私有の開発履歴は含みません。公開範囲は [PUBLIC-RELEASE.md](PUBLIC-RELEASE.md) を参照してください。

## 含まれるskills

| Skill | 役割 |
|---|---|
| [`write-research-paper`](skills/write-research-paper/SKILL.md) | 著者の指示に沿った数学論文の執筆・改訂、執筆側での説明の点検、指摘の整理と修正 |
| [`read-research-paper`](skills/read-research-paper/SKILL.md) | 明示的に委任された、固定版原稿の独立した説明レビュー。原稿は編集しません |
| [`latex-paragraph-ids`](skills/latex-paragraph-ids/SKILL.md) | LaTeX原稿の段落に固定IDを導入・維持し、IDを指定した検索や編集を支援 |

執筆と通常の点検・修正は、一つのエージェントで進める構成です。独立レビューは著者が明示的に委任した場合に使います。レビューには、順に初読する `continuous`、原稿全体の説明を検討する `editorial`、指定した修正箇所を確認する `delta` の3モードがあります。

執筆用と読者用は共通の説明基準を相対パスで参照するため、**2つを一緒に導入し、リポジトリ内の配置を保ってください。** 説明のレビュー、証明の正しさ、原稿のビルド成功は別の確認です。

## 導入

安定した保存先に、このリポジトリを一度クローンします。

```sh
git clone https://github.com/yoshito-ishiki-math/math-paper-skills.git
```

以下の `/absolute/path/to/math-paper-skills` は、クローン先の絶対パスに置き換えてください。既に同名のskillを使っている場合は、リンク先とローカル変更を確認してから切り替えます。

### Codexなどの共通skillディレクトリ

```sh
mkdir -p "$HOME/.agents/skills"
ln -sfn /absolute/path/to/math-paper-skills/skills/write-research-paper \
  "$HOME/.agents/skills/write-research-paper"
ln -sfn /absolute/path/to/math-paper-skills/skills/read-research-paper \
  "$HOME/.agents/skills/read-research-paper"
```

段落IDも使う場合は、次のリンクを追加します。

```sh
ln -sfn /absolute/path/to/math-paper-skills/skills/latex-paragraph-ids \
  "$HOME/.agents/skills/latex-paragraph-ids"
```

### Claude Code

```sh
mkdir -p "$HOME/.claude/skills"
ln -sfn /absolute/path/to/math-paper-skills/skills/write-research-paper \
  "$HOME/.claude/skills/write-research-paper"
ln -sfn /absolute/path/to/math-paper-skills/skills/read-research-paper \
  "$HOME/.claude/skills/read-research-paper"
```

段落IDを使う場合は、同じ方法で `latex-paragraph-ids` もリンクします。別のホストを使う場合は、そのホストのskill探索先に合わせてください。一つのクローンを共通の参照先にし、各研究プロジェクトへskill本体を複製しない運用を想定しています。

## 使い方

Codexでは `$write-research-paper`、Claude Codeでは `/write-research-paper` のように指定できます。ホストが説明文から適切なskillを選択する場合もあります。導入や更新が反映されない場合は、新しいセッションを開始するか、ホストの再読み込み方法を確認してください。

依頼例は次のとおりです。

- 「この原稿の第2節を改訂して。数学的な主張は保ち、変更箇所を説明して」
- 「この固定版原稿を、独立した読者にeditorialモードでレビューさせて。原稿は変更しないで」
- 「このLaTeX原稿に段落IDを導入して」

対象原稿と依頼範囲を伝えてください。独立レビューでは、固定する版、読者が見てよい資料、出力先などをプロトコルに沿って整理します。skillを導入しただけでは、原稿編集、別エージェントへの委任、投稿・公開の許可にはなりません。

## 著者スタイルの集約

著者共通の文体・引用・ソース整形などの方針は、このskill群などを入口として、**一つの共通プロファイルに集約することを推奨します。** 各ハーネスにはその参照先を、各原稿の `STYLE.md` には原稿固有の指定を置きます。

公開版の [`author-style.md`](skills/write-research-paper/references/author-style.md) は、個人の好みを含まない設定案内です。実際のプロファイルは私有のskill拡張または共通ファイルで管理し、公開リポジトリへコミットしないでください。ハーネス側では、例えば無視対象の `docs/STYLE.local.md` から共通ファイルを指定できます。独立した読者には、許可された固定版のスタイル指定だけを渡します。

著者プロファイルを指定しない場合でも、明示的な指示、原稿の既存の慣習、投稿先の要件と共通の執筆指針に沿って作業できます。

### 任意採用の具体例

[著者スタイルの例](examples/author-style.md)には、実際の運用プロファイルから個人を特定する情報や論文固有の参照を除いた、具体的な方針を収録しています。句読法、`give`・`suppose` などの語法、定理と証明の説明、量化と依存関係、記号、文献・相互参照、TeXソース整形などが対象です。

**skillの導入だけでは自動適用されません。** 数学英語の普遍的な正誤基準ではなく、一つのスタイルの見本です。必要な規則を私有の共通プロファイルへコピーして調整し、利用するプロファイルとして明示的に指定してください。用例は一般的な記号・TeX設定で、原稿からの引用は含みません。

## ハーネス・Kichoとの組み合わせ

[math-research-harness-public](https://github.com/yoshito-ishiki-math/math-research-harness-public) と組み合わせて使えます。skillsは汎用の執筆・説明レビューを担当し、ハーネスは研究記録、原稿の状態、検査、投稿準備などのプロジェクト固有の運用を担当します。

公開ハーネスでは、各原稿を `paperN/` の独立したKichoプロジェクトとして扱い、`kicho init`、`check`、`build`、`archive`、`flatten`、`submit` などを使う手順を定めています。Kicho本体はこのリポジトリに同梱していません。別の原稿管理環境では、そのプロジェクトの指示と検査手順に従ってください。

## 任意のコーパスツール

執筆用skillには、私有の論文コーパスから語彙や用例を検索・集計するPythonツールも含まれています。Python 3.10以降の標準ライブラリを使い、入力・出力先を明示して実行します。詳細は [`corpus-method.md`](skills/write-research-paper/references/corpus-method.md) を参照してください。

原稿、コーパスの設定、個人向けの語彙候補、生成済み索引は同梱しません。生成結果には原文の抜粋やパスが含まれるため、コードとは別に私有データとして管理します。使用頻度は参考資料であり、語の禁止リストや著者の現在の指示を置き換えるものではありません。

## 更新と検査

クローン先で `git pull` を実行すると、各リンク先も更新版を参照します。私有の変更がある場合は、先に差分を確認してください。再現性が必要な原稿作業では、使用したskillのコミットを記録するか、確認済みの版を固定します。

同梱ツールとskill内の参照先は、架空の入力を用いて確認できます。

```sh
python3 -m unittest discover -s tests
```

この検査は論文の数学的正しさや、すべての文書クラスでの段落IDの表示を保証するものではありません。原稿のビルドや表示は、そのプロジェクトで確認してください。

## ライセンス

MITライセンスです。[LICENSE](LICENSE) を参照してください。
