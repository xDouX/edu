from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("sqlite:///users.db")

Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
