from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base_model import BaseModel
from datetime import datetime


class Match(BaseModel):
    __tablename__ = 'MATCHES'
    id_team_sport_1 = Column('id_team_sport_1', Integer, nullable=False, 
                            ForeignKey('TEAM_SPORT.id'))
    team_sport_1 = relationship('TEAM_SPORT')
    id_team_sport_2 = Column('id_team_sport_2', Integer, nullable=False, 
                            ForeignKey('TEAM_SPORT.id'))
    team_sport_2 = relationship('TEAM_SPORT')
    match_date = Column('match_date', DateTime , nullable=False)
    score_team_1 = Column('score_team_1', Integer , nullable=False)
    score_team_2 = Column('score_team_2', Integer , nullable=False)

    def __init__(self, id_team_sport_1: int, id_team_sport_2: int, 
                    match_date: datetime, score_team_1: int, 
                    score_team_2: int) -> None:
        self.id_team_sport_1 = id_team_sport_1
        self.id_team_sport_2 = id_team_sport_2
        self.match_date = match_date
        self.score_team_1 = score_team_1
        self.score_team_2 = score_team_2