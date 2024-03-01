from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv("DB_URI").replace("postgres://", f"postgresql://")


def db_connect():
    engine = create_engine(DB_URI)
    engine.connect()
    return engine
