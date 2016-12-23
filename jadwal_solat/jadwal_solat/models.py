from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from jadwal_solat import settings
 
DeclarativeBase = declarative_base()
 
def db_connect():
    return create_engine(URL(**settings.DATABASE))
 
 
def create_jadwal_solat_table(engine):
    DeclarativeBase.metadata.create_all(engine)
 
 
class JadwalSolat(DeclarativeBase):
    __tablename__ = 'jadwal_solat'
 
    id = Column(Integer, primary_key=True)
    idKota = Column(String(300))
    namaKota = Column(String(300))
    hari = Column(String(300))
    shubuh = Column(String(300))
    terbit = Column(String(300))
    dzuhur = Column(String(300))
    ashar = Column(String(300))
    magrib = Column(String(300))
    isya = Column(String(300))
    