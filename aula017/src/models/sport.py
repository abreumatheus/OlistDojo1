from sqlalchemy import Column, Integer, String
from src.models.base_model import BaseModel

class Sport(BaseModel):
    __tablename__ = 'sport'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    
    def __init__(self,name:str, description:str) -> None:
        self.name = name
        self.description =  description
