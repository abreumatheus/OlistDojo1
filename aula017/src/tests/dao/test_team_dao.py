from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.team_dao import TeamDao
from src.models.team import Team
import pytest


class TestTeamDao:
    @pytest.fixture
    def create_instance(self):
        team = Team('Um nome', 'Uma descrição')
        return team

    def test_instance(self):
        team_dao = TeamDao()
        assert isinstance(team_dao, TeamDao)

    def test_save(self, create_instance):
        team_saved = TeamDao().save(create_instance)

        assert team_saved.id_ is not None
        TeamDao().delete(team_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            team_saved = TeamDao().save('team')

    def test_read_by_id(self, create_instance):
        team_saved = TeamDao().save(create_instance)
        team_read = TeamDao().read_by_id(team_saved.id_)

        assert isinstance(team_read, Team)
        TeamDao().delete(team_saved)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            team_read = TeamDao().read_by_id('team_saved.id_')

    def test_read_all(self):
        team_read = TeamDao().read_all()

        assert isinstance(team_read, list)

    def test_delete(self, create_instance):
        team_saved = TeamDao().save(create_instance)
        team_read = TeamDao().read_by_id(team_saved.id_)
        TeamDao().delete(team_read)
        team_read = TeamDao().read_by_id(team_saved.id_)

        assert team_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            TeamDao().delete('team_read')
