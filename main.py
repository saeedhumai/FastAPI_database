import models
from fastapi import FastAPI, Depends
from database import engine
from models import Todo
from typing import Annotated
from database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()

@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
   return db.query(models.Todo).all()

