import sys
sys.path.append('.')

import pytest
from src.controllers.base_controller import BaseController
from src.controllers.team_sport_controller import TeamSportController
from src.models.team_sport import TeamSport


class TestTeamSportController:
    @pytest.fixture
    def create_instance(self):
        team_sport = TeamSportController()
        return team_sport

    @pytest.fixture
    def create_team_sport(self):
        team_sport = TeamSport(1, 1)
        return team_sport

    def test_team_sport_controller_instance(self, create_instance):
        assert isinstance(create_instance, BaseController)
        assert isinstance(create_instance, TeamSportController)

    def test_team_sport_read_all(self, create_instance):
        result = create_instance.read_all()
        assert isinstance(result, list)

    def test_team_sport_read_by_id(self, create_team_sport):
        create = TeamSportController().create(create_team_sport)
        read = TeamSportController().read_by_id(create.id_)
        assert isinstance(read, TeamSport)
        TeamSportController().delete(read)
        
    def test_team_sport_delete(self, create_team_sport):
        create = TeamSportController().create(create_team_sport)
        TeamSportController().delete(create)
        with pytest.raises(Exception):
            read = TeamSportController().read_by_id(create.id_)

    def test_team_sport_create(self, create_team_sport):
        create = TeamSportController().create(create_team_sport)
        assert create.id_team == 1
        assert create.id_sport == 1
        assert isinstance(create, TeamSport)

    def test_team_sport_not_create(self):
        with pytest.raises(TypeError):
            create = TeamSportController().create('error')

    def test_team_sport_update(self, create_team_sport):
        create = TeamSportController().create(create_team_sport)
        create.id_team = 2
        create.id_sport = 2
        update = TeamSportController().update(create)
        assert update.id_team == 2
        assert update.id_sport == 2
        assert isinstance(update, TeamSport)

    def test_team_sport_not_update(self):
        with pytest.raises(Exception):
            create = TeamSportController().update('error')