from sqlalchemy import Column, Float, String, Integer, ForeignKey
from src.models.base_model import BaseModel
from sqlalchemy.orm import relationship

class Bet(BaseModel):
    __tablename__ = 'bet'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)
    customer_id = Column('customer_id', Integer, ForeignKey('customer.id') ) 
    customer = relationship('customer')
    match_id = 
    match = 
    team_id = 
    team = 
    value_bet = Column('value_bet', Float, nullable=True)

    def __init__(self,name:str, description:str) -> None:
        self.name = name
        self.description =  description
