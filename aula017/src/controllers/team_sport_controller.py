from src.controllers.base_controller import BaseController
from src.dao.team_sport_dao import TeamSportDao
from src.controllers.sport_controller import SportController
from src.controllers.team_controller import TeamController
from src.models.team_sport import TeamSport

class TeamSportController(BaseController):
    def __init__(self):
        super().__init__(TeamSportDao)

    def create(self, model: TeamSport) -> TeamSport:
        sport_controller = SportController()
        sport = sport_controller.read_by_id(model.id_sport)
        team_controller = TeamController()
        team = team_controller.read_by_id(model.id_team)
        if sport and team:
            dao = TeamSportDao()
            return dao.save(model)
        
    
    def update(self, model: TeamSport) -> TeamSport:
        sport_controller = SportController()
        sport = sport_controller.read_by_id(model.id_sport)
        team_controller = TeamController()
        team = team_controller.read_by_id(model.id_team)
        if sport and team:
            dao = TeamSportDao()
            dao.save(model)
            return dao.save(model)
            
        
        