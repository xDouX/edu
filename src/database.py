from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

engine = create_engine(settings.DATABASE_URL_psycopg)

Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
