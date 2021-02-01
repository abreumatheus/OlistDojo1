from sqlalchemy import Column, Integer
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import ForeignKey
from src.models.base_model import BaseModel
from src.utils.validators import validate_type
from src.models.team import Team
from src.models.sport import Sport


class TeamSport(BaseModel):
    __tablename__ = 'TEAM_SPORT'
    id_sport = Column('id_sport', Integer, ForeignKey(
        'SPORT.id'), nullable=False)
    sport = relationship('Sport')
    id_team = Column('id_team', Integer, ForeignKey('TEAM.id'), nullable=False)
    team = relationship('Team')

    def __init__(self, id_sport: int, id_team: int) -> None:
        self.id_sport = id_sport
        self.id_team = id_team

    @validates('id_sport')
    def validate_id_sport(self, key, id_sport):
        return validate_type(id_sport, int, key)

    @validates('id_team')
    def validate_id_team(self, key, id_team):
        return validate_type(id_team, int, key)
