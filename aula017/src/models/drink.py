from sqlalchemy import Column, String, Integer
from src.models.base_model import BaseModel


class Drink(BaseModel):
    __tablename__ = 'drink'
    name = Column('name', String(length=100), nullable=False)
    volume = Column('volume', Integer, nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self,name:str, volume:int, description:str) -> None:
        self.name = name
        self.volume = volume
        self.description =  description
