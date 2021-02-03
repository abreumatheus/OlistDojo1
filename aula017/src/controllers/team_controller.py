from src.controllers.base_controller import BaseController
from src.dao.team_dao import TeamDao


class TeamController(BaseController):
    def __init__(self):
        self.__dao = TeamDao()
        super().__init__(self.__dao)
