import sys
sys.path.append('.')
from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from src.models.base_model import BaseModel


class Team(BaseModel):
    __tablename__ = 'TEAM'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self,name:str, description:str) -> None:
        self.name = name
        self.description =  description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name isn't string")
        if not name.strip(): # tanto '' quanto None
            raise ValueError("Name can't be empty")
        if len(name) > 100:
            raise ValueError("Name can't be more than 100 characters")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description isn't string")
        if len(description) > 255:
            raise ValueError("Description can't be more than 255 characters")
        return description
