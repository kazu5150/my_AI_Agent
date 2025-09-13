# My AI Agent

OpenAI APIを使用したAIエージェントプロジェクトです。

## 概要

このプロジェクトは、OpenAIのGPT-4o-miniモデルを使用してチャット補完機能を実装したPythonアプリケーションです。章ごとに構成された学習用プロジェクトとして設計されています。

## 機能

- OpenAI APIを使用したチャット補完
- 環境変数を使用したAPIキー管理
- トークン使用量の表示

## セットアップ

### 前提条件

- Python 3.7以上
- OpenAI APIキー

### インストール手順

1. リポジトリをクローン
```bash
git clone https://github.com/kazu5150/my_AI_Agent.git
cd my_AI_Agent
```

2. 仮想環境の作成と有効化
```bash
python -m venv myenv
source myenv/bin/activate  # Windowsの場合: myenv\Scripts\activate
```

3. 依存関係のインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
```bash
cp .env.example .env
```

`.env`ファイルを編集してOpenAI APIキーを設定してください：
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 使用方法

### チャット補完の実行

```bash
cd chapter3
python chat_completions.py
```

## プロジェクト構成

```
my_AI_Agent/
├── README.md              # このファイル
├── CLAUDE.md             # Claude Code用の開発ガイド
├── requirements.txt      # Python依存関係
├── .env.example         # 環境変数テンプレート
├── .env                 # 環境変数（.gitignoreで除外）
├── .gitignore           # Git除外設定
├── chapter3/            # 第3章のコード
│   ├── chat_completions.py    # チャット補完の基本実装
│   ├── structured_output.py   # 構造化出力の例
│   └── structured_output2.py  # 構造化出力の例2
└── myenv/               # Python仮想環境（.gitignoreで除外）
```

## 依存関係

- `openai>=1.0.0` - OpenAI Python クライアントライブラリ
- `python-dotenv>=1.0.0` - 環境変数の読み込み

## 注意事項

- `.env`ファイルにはAPIキーが含まれるため、Gitにコミットしないでください
- OpenAI APIの使用には料金が発生します
- APIキーは安全に管理してください

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 貢献

プルリクエストやIssueは歓迎します。