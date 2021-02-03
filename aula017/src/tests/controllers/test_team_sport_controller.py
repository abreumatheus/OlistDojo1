import pytest
from src.controllers.base_controller import BaseController
from src.controllers.team_sport_controller import TeamSportController
from src.models.team_sport import TeamSport

@pytest.fixture
def create_instance():
    team_sport = TeamSportController()
    return team_sport

def test_team_sport_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, TeamSportController)

def test_team_sport_read_all(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)

def test_team_sport_read_by_id():
    model = TeamSport(1, 1)
    model = TeamSportController().create(model)
    print(type(model.id_), 'uma string muuuuuuuiiiiitoooo grande')
    model = TeamSportController().read_by_id(id_=model.id_)
    assert isinstance(model, TeamSport)
    TeamSportController.delete(model)
    