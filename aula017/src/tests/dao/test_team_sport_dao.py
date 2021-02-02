from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.team_sport_dao import TeamSportDao
from src.models.team_sport import TeamSport
import pytest


class TestTeamSportDao:
    def test_instance(self):
        team_sport_dao = TeamSportDao()
        assert isinstance(team_sport_dao, TeamSportDao)

    def test_save(self):
        team_sport = TeamSport(1, 1)
        team_sport_saved = TeamSportDao().save(team_sport)

        assert team_sport_saved.id_ is not None
        TeamSportDao().delete(team_sport_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            team_sport_saved = TeamSportDao().save('team_sport')

    def test_read_by_id(self):
        team_sport = TeamSport(1, 1)
        team_sport_saved = TeamSportDao().save(team_sport)
        team_sport_read = TeamSportDao().read_by_id(team_sport_saved.id_)

        assert isinstance(team_sport_read, TeamSport)
        TeamSportDao().delete(team_sport_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            team_sport_read = TeamSportDao().read_by_id('team_sport_saved.id_')

    def test_read_all(self):
        team_sport_read = TeamSportDao().read_all()

        assert isinstance(team_sport_read, list)

    def test_delete(self):
        team_sport = TeamSport(1, 1)
        team_sport_saved = TeamSportDao().save(team_sport)
        team_sport_read = TeamSportDao().read_by_id(team_sport_saved.id_)
        TeamSportDao().delete(team_sport_read)
        team_sport_read = TeamSportDao().read_by_id(team_sport_saved.id_)

        assert team_sport_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            TeamSportDao().delete('team_sport_read')
