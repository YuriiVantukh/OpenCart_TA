"""
Creates a session and defines the class BASE
from which other ORM classes will be inherited.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from helpers.settings import BASE_CONNECTION


ENGINE = create_engine(BASE_CONNECTION)
SESSION = sessionmaker(bind=ENGINE)
BASE = declarative_base()


def session_factory():
    """
    Create all tables stored in this metadata.
    """
    BASE.metadata.create_all(ENGINE)
    return SESSION()
