from sqlalchemy import Column, Float, String, Integer, ForeignKey
from src.models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates

from src.utils.validators import validate_type, validate_not_empty, validate_len, validate_be_greater_than_zero


class Bet(BaseModel):
    __tablename__ = 'BET'
    id_customer = Column('id_customer', Integer, ForeignKey('CUSTOMER.id'))
    customer = relationship('CUSTOMER')
    id_match = Column('id_match', Integer, ForeignKey('MATCHES.id'))
    match = relationship('MATCHES')
    id_team_sport = Column('id_team_sport', Integer, ForeignKey('TEAM_SPORT.id'))
    team = relationship('TEAM_SPORT')
    bet_value = Column('bet_value', Float, nullable=True)

    def __init__(self, id_customer: int, id_match: int, id_team_sport: int, bet_value: float) -> None:
        self.id_customer = id_customer
        self.id_match = id_match
        self.id_team_sport = id_team_sport
        self.bet_value = bet_value

    @validates('id_customer')
    def validate_id_customer(self, key, id_customer):
        id_customer = validate_type(id_customer, int, key)
        return id_customer

    @validates('id_match')
    def validate_id_match(self, key, id_match):
        id_match = validate_type(id_match, int, key)
        return id_match

    @validates('id_team_sport')
    def validate_id_team_sport(self, key, id_team_sport):
        id_team_sport = validate_type(id_team_sport, int, key)
        return id_team_sport

    @validates('bet_value')
    def validate_bet_value(self, key, bet_value):
        bet_value = validate_type(bet_value, float, key)
        bet_value = validate_be_greater_than_zero(bet_value, key)
        return bet_value
