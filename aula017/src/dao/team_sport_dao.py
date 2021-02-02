from src.dao.base_dao import BaseDao
from src.models.team_sport import TeamSport


class TeamSportDao(BaseDao):
    def __init__(self):
        super().__init__(TeamSport)
