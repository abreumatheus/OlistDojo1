from src.dao.base_dao import BaseDao
from src.models.bet import Bet


class BetDao(BaseDao):
    def __init__(self):
        super().__init__(Bet)
