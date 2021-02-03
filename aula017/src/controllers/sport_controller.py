from src.controllers.base_controller import BaseController
from src.dao.sport_dao import SportDao


class SportController(BaseController):
    def __init__(self):
        self.__dao = SportDao()
        super().__init__(self.__dao)