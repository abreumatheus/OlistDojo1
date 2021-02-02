from src.dao.base_dao import BaseDao
from src.models.team import Team


class TeamDao(BaseDao):
    def __init__(self):
        super().__init__(Team)
