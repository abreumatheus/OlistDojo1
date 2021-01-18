from sqlalchemy import Column, String
from .base_model import BaseModel


class Category(BaseModel): 
    __tablename__ = 'category'

    name = Column( String(length=200) )
    description = Column( String(length=200) )

    def __init__(self, name:str, description:str):
        self.name = name
        self.description = description

