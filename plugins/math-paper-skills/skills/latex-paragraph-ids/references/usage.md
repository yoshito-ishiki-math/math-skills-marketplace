# 段落IDの管理をKichoへ移す

`paragraphids.sty` と補助ツールはKichoが管理します。このskillにはパッケージや実装コードを置きません。

`kicho help paraids` と、Kichoの `docs/paragraphids.md` を参照してください。導入には `kicho paraids install --root <paper>` を使います。既存のIDと原稿側のパッケージの版を保持し、無関係な原稿へ一括導入しません。

著者の編集規約と提出時の確認事項は [SKILL.md](../SKILL.md) に記載しています。提出用コピーのID・注記を無効化する処理は、Kichoの `submit` と `submit --arxiv` が担当します。
