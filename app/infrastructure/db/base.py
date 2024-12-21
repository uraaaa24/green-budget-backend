from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# PostgreSQL接続用のデータベースURL
DATABASE_URL = "postgresql://user:password@postgres_host:5432/dbname"

# エンジン
engine = create_engine(DATABASE_URL)

# セッションローカル
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラス
Base = declarative_base()
