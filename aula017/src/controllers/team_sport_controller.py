from src.controllers.base_controller import BaseController
from src.dao.team_sport_dao import TeamSportDao
from src.controllers.sport_controller import SportController
from src.controllers.team_controller import TeamController
from src.models.team_sport import TeamSport

class TeamSportController(BaseController):
    def __init__(self):
        self.__dao = TeamSportDao()
        super().__init__(self.__dao)

    def create(self, model: TeamSport) -> TeamSport:
        sport = SportController().read_by_id(model.id_sport)
        team = TeamController().read_by_id(model.id_team)
        return self.__dao.save(model)        
    
    def update(self, model: TeamSport) -> TeamSport:
        sport = SportController().read_by_id(model.id_sport)
        team = TeamController().read_by_id(model.id_team)
        return self.__dao.save(model)
        