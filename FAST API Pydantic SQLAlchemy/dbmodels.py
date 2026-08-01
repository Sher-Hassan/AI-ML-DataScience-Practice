
# We will use Base of SQL Alchemy instead of BaseModel of Pydantic
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# So we use = Column(<define attr>) to define 

class Product(Base): 

    __tablename__= "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)