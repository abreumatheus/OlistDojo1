from backend.model.base_model import BaseModel
from sqlalchemy import String, Column, Float


class Product(BaseModel):
    __tablename__ = 'products'

    name = Column( 'name', String(length=50), nullable=False )
    description = Column( 'description', String(length=150), nullable=False )
    price = Column( 'price', Float, nullable=False )

    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

