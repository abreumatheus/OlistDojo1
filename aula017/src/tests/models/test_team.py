import sys
sys.path.append('.')
from src.models.team import Team
import pytest

@pytest.fixture
def create_object():
    return Team('as', 'Melhor time do Brasil')

def test_name_not_none(create_object):
    with pytest.raises(TypeError):
        create_object
   

def test_name_not_str():
    try:
        team = Team(10, 'Melhor time do Brasil')
        raise NotImplementedError('Exception not raised')
    except Exception as error:
        assert isinstance(error, TypeError)

