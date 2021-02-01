from src.models.match import Match
from datetime import datetime
import pytest

@pytest.mark.parametrize('id_team_sport_1, id_team_sport_2,\
                        match_date, score_team_1, score_team_2',
                        [('test', 2, datetime.today(), 10, 12),
                        (10, 'test', datetime.today(), 10, 12),
                        (10, 2, None, 10, 12), (10, 2, datetime.today(), 'ttttt', 12),
                        (10, 2, datetime.today(), 10, 'ttttt')
                        ])

def test_match_type(id_team_sport_1, id_team_sport_2, match_date,
                        score_team_1, score_team_2):
    with pytest.raises(TypeError):
        matches = Match(id_team_sport_1, id_team_sport_2, match_date,
                        score_team_1, score_team_2)
