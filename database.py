from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from Constantes import DATABASE


engine = create_engine(DATABASE)

localSession = sessionmaker(engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass


def getDB():
    db = localSession()

    try:
        yield db
    finally:
        db.close()