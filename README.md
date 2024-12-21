```bash
.
├── Dockerfile
├── Makefile
├── docker-compose.yml
├── requirements.txt
├── .env                                              # 環境変数ファイル (DB接続情報や秘密鍵を管理)
├── app/
│   ├── main.py                                      # アプリケーションエントリーポイント
│   ├── core/                                        # 基盤設定 (アプリ全体で利用される共通ロジック)
│   │   ├── config.py                               # 環境変数や設定値の管理
│   │   ├── logger.py                               # ログ設定
│   │   └── [その他の共通ロジック]
│   ├── domain/                                      # ドメイン層 (ビジネスロジックの中心)
│   │   ├── repository/                             # リポジトリインターフェース
│   │   │   └── [リポジトリインターフェースファイル]
│   │   └── [エンティティや値オブジェクト]
│   ├── infrastructure/                              # インフラ層 (データベースや外部システム連携)
│   │   ├── db/                                     # データベース関連
│   │   │   ├── base.py                            # DB接続設定とSQLAlchemyのBaseクラス
│   │   │   ├── init_db.py                         # 初期データ作成やテーブル作成スクリプト
│   │   │   └── models/                            # DBモデル
│   │   │       └── [SQLAlchemyモデルファイル]
│   │   └── repositories/                           # リポジトリの具体的な実装
│   │       └── [リポジトリ実装ファイル]
│   ├── interfaces/                                  # 外部システムとのインターフェース層 (必要に応じて)
│   │   └── [外部APIやサービス連携用ファイル]
│   ├── presentation/                                # プレゼンテーション層 (FastAPIのルートやエンドポイント)
│   │   └── [APIルーターファイル (例: transaction_router.py)]
│   ├── schemas/                                     # スキーマ層 (入出力データの定義)
│   │   └── [Pydanticスキーマファイル]
│   └── usecases/                                    # ユースケース層 (アプリ固有の操作ロジック)
│       └── [ユースケースクラスファイル (例: transaction_usecase.py)]
└── tests/                                            # テストディレクトリ
    ├── conftest.py                                   # pytestの共通設定やフィクスチャ
    └── [テストコードファイル]
```
