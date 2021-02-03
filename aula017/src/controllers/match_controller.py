from src.controllers.base_controller import BaseController
from src.controllers.team_controller import TeamController
from src.dao.match_dao import MatchDao
from src.models.match import Match


class MatchController(BaseController):
    def __init__(self):
        self.__dao = MatchDao()
        self.__team_controller = TeamController()
        super().__init__(self.__dao)

    def create(self, model: Match) -> Match:
        self.validate(model)
        return super().create(model)

    def update(self, model: Match) -> Match:
        self.validate(model)
        return super().update(model)

    def validate(model: Match) -> None:
        try:
            self.__team_controller.read_by_id(model.id_team_sport_1)
            self.__team_controller.read_by_id(model.id_team_sport_2)
        except:
            raise Exception("Team sport 1 and Team sport 2 must exist.")
