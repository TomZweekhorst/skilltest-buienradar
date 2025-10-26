# src/db_models.py
from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Text, ForeignKey, create_engine, UniqueConstraint
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class Measurement(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(Integer, ForeignKey("stations.id"), index=True)
    observed_at = Column(DateTime, index=True)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    precipitation = Column(Float, nullable=True)
    wind_speed = Column(Float, nullable=True)
    wind_direction = Column(Float, nullable=True)
    raw = Column(Text)  # raw JSON string if you want to keep it
    station = relationship("Station")
    __table_args__ = (UniqueConstraint('station_id', 'observed_at', name='uq_station_time'),)

def get_engine():
    """Return SQLAlchemy engine based on env. Defaults to SQLite project DB for reproducibility."""
    db_url = os.getenv("DB_URL")
    if db_url:
        return create_engine(db_url, future=True)
    # default to sqlite file in project folder
    db_path = os.getenv("SQLITE_PATH", "data/snapshot.db")
    return create_engine(f"sqlite:///{db_path}", future=True)

def create_all_tables(engine):
    Base.metadata.create_all(engine)
