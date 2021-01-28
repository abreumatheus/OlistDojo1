from sqlalchemy import Column, Float, String, Integer, ForeignKey
from src.models.base_model import BaseModel
from sqlalchemy.orm import relationship

class Bet(BaseModel):
    __tablename__ = 'BET'    
    id_customer = Column('id_customer', Integer, ForeignKey('CUSTOMER.id') ) 
    customer = relationship('CUSTOMER')
    id_match = Column('id_match', Integer, ForeignKey('MATCHES.id') ) 
    match = relationship('MATCHES')
    id_team_sport = Column('id_team_sport', Integer, ForeignKey('TEAM_SPORT.id') ) 
    team = relationship('TEAM_SPORT')
    bet_value = Column('bet_value', Float, nullable=True)

    def __init__(self,id_customer: int, id_match: int, id_team_sport: int, bet_value: float) -> None:
        self.id_customer = id_customer
        self.id_match =  id_match
        self.id_team_sport = id_team_sport
        self.bet_value = bet_value
