from database import base #base class is defined in database.py which is setting it up 
from sqlalchemy import column , integer ,string , bolean # import for making table from sqlalchemy 
class Todo(base): # class definitly from table 
   __tablename__="Todo" 
   id = column(integer, primary_key=True,index=True)
   title = column(string )
   description =column(string)
   priority = column(integer)
   complete= column(bolean, default=False)



