from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class DataEntry(Base):
    __tablename__ = "dataEntries"

class DataStation(Base):
    __tablename__ = "DataStation"

class DataGrouping(Base):
    __tablename__ = "dataGrouping"


