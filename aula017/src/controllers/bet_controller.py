from src.controllers.base_controller import BaseController
from src.dao.bet_dao import BetDao


class BetController(BaseController):
    def __init__(self):
        self.__dao = BetDao()
        super().__init__(self.__dao)
