from sqlalchemy import Column, Integer, String
from src.models.base_model import BaseModel

class Customer(BaseModel):
    __tablename__ = 'customer'
    name = Column('name', String(length=100), nullable=False)
    num_doc = Column('num_doc', String(length=50), nullable=False)
    phone = Column('phone', String(length=20), nullable=True)
    
    def __init__(self,name:str, num_doc:str, phone:str) -> None:
        self.name = name
        self.num_doc =  num_doc
        self.phone =  phone
