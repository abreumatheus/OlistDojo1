from src.dao.base_dao import BaseDao
from src.models.match import Match


class MatchDao(BaseDao):
    def __init__(self):
        super().__init__(Match)
