from connection import data 
from models import Product ,Base

Base.metadata.create_all(bind=data)
