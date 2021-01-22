from backend.model.base_model import BaseModel
from sqlalchemy import String, Column


class Category(BaseModel):
    __tablename__ = 'categories'

    name = Column( 'name', String(length=200), nullable=False )
    description = Column( 'description', String(length=200) )

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description