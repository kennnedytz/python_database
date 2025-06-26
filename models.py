from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(String(100))

    def __init__(self, name, price):
        self.name = name
        self.price = price