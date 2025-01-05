from database import Base #base class is defined in database.py which is setting it up 
# from sqlalchemy import column , integer ,string , bolean # import for making table from sqlalchemy 
from sqlalchemy import Column, Integer, String, Boolean



class Todo(Base): # class definitly from table 
   __tablename__="Todo" 
   id = Column(Integer, primary_key=True,index=True)
   title = Column(String )
   description =Column(String)
   priority = Column(Integer)
   complete= Column(Boolean, default=False)



