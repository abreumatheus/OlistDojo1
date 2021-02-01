from src.utils.validators import validate_not_empty, validate_type
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from src.models.base_model import BaseModel
from datetime import datetime
from sqlalchemy.orm import validates
from src.models.team_sport import TeamSport


class Match(BaseModel):
    __tablename__ = 'MATCHES'
    id_team_sport_1 = Column('id_team_sport_1', Integer,
                             ForeignKey('TEAM_SPORT.id'), nullable=False)
    team_sport_1 = relationship('TeamSport')
    id_team_sport_2 = Column('id_team_sport_2', Integer,
                             ForeignKey('TEAM_SPORT.id'), nullable=False)
    team_sport_2 = relationship('TeamSport')
    match_date = Column('match_date', DateTime, nullable=False)
    score_team_1 = Column('score_team_1', Integer, nullable=False)
    score_team_2 = Column('score_team_2', Integer, nullable=False)

    def __init__(self, id_team_sport_1: int, id_team_sport_2: int,
                 match_date: datetime, score_team_1: int,
                 score_team_2: int) -> None:
        self.id_team_sport_1 = id_team_sport_1
        self.id_team_sport_2 = id_team_sport_2
        self.match_date = match_date
        self.score_team_1 = score_team_1
        self.score_team_2 = score_team_2

    @validates('id_team_sport_1')
    def validate_id_team_sport_1(self, key, id_team_sport_1):
        return validate_type(id_team_sport_1, int, key)

    @validates('id_team_sport_2')
    def validate_id_team_sport_2(self, key, id_team_sport_2):
        return validate_type(id_team_sport_2, int, key)

    @validates('match_date')
    def validate_match_date(self, key, match_date):
        return validate_type(match_date, datetime, key)

    @validates('score_team_1')
    def validate_score_team_1(self, key, score_team_1):
        return validate_type(score_team_1, int, key)

    @validates('score_team_2')
    def validate_score_team_2(self, key, score_team_2):
        return validate_type(score_team_2, int, key)
