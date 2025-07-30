from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creating url 
Database_url="sqlite:///./shopsmart.db"

#using mysqllite
engine=create_engine(Database_url,connect_args={"check_same_thread":False})

#session creation
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#base declare
Base=declarative_base()


