from src.models.team_sport import TeamSport
import pytest


@pytest.mark.parametrize('id_sport,id_team', [(1, 2), (3, 4), (5, 2)])
def test_team_sport_type(id_sport, id_team):
    with pytest.raises(TypeError):
        team_sport = TeamSport(id_sport, id_team)
