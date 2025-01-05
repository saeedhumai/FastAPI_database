from sqlalchemy import create_enginer
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declerative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
sessionmaker = sessionmaker(autocommit=False , autoflush=False, bind=engine)

base=declarative_base()



