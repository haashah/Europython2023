from sqlalchemy import create_engine, Column, Integer,
from sqlalchemy import sessionmaker, declarative_base
DATABASE_URL = "sqlite:///./gotham_database.db"

engine = create_engine(DATABASE_URL): Engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(): Type[_DeclarativeBase]

class Crime(Base):
    __tablename__ = "crimes" : str

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String) : Column[str]
    description = Column(String) 
    location = Column(String)
    date = Column(DateTime) 
    latitute = Column(Float) 
    longitude = Column(Float)




  
