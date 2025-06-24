from sqlalchemy import Column,interger,String,database
from sqlalchemy.orm import declarative_base
from date import date
Base=declarative_base
class products(Base):
    __tablename__=="products"

id=Column(Interger,primary key=True,auto_inrement=True,nullable=false)
name=Column(String(100),nullable=False)
date_applied=Column(date,default=date.today)
def__init__(self,name,date):
    self.name=name
    self.date=date