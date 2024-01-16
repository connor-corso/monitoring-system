from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://monitoring-system-backend:" + str(os.environ['DATABASE_PASSWORD']) + "@" + str(os.environ['DATABASE_URL'])

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)

SessionLocal = sessionmaker(autocommt=False, autoflush=False, bind=engine)

Base = declarative_base()