from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
username="root"
password="2480"
database="products"
path=f"mysql+mysqldb://{username}:{password}@localhost/{database}"
data=create_engine(path)
session=sessionmaker(bind=data)
session=session()