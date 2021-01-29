import sys
sys.path.append('.')
from src.models.team import Team
import pytest


@pytest.mark.parametrize("name, description", [
                            ('N',''), 
                            ('N'*100,'D'*255), 
                            ('N'*50,'D'*120)
                        ])
def test_team_instance(name, description):
    team = Team(name, description)
    assert isinstance(team, Team)

def test_name_min_len():
    name = 'C'
    description = ''
    team = Team(name, description)
    assert team.name is name

def test_name_not_none():
    with pytest.raises(TypeError):
        team = Team(None, 'Melhor time do Brasil')

@pytest.mark.parametrize("name, description", [
                            (10,'Melhor time do Brasil'), 
                            (10.5,'Melhor time do Brasil'), 
                            (False,'Melhor time do Brasil')
                        ])
def test_name_not_str(name, description):
    with pytest.raises(TypeError):
        team = Team(name, description)

def test_name_not_empty():
    with pytest.raises(ValueError):
        team = Team('', 'Melhor time do Brasil')

def test_name_max_len():
    with pytest.raises(ValueError):
        team = Team('Co'*51, 'Melhor time do Brasil')

def test_description_min_len():
    name = 'C'
    description = ''
    team = Team(name, description)
    assert team.description is description

def test_description_not_none():
    with pytest.raises(TypeError):
        team = Team('Metropolitano', None)

def test_description_not_str():
    with pytest.raises(TypeError):
        team = Team('Metropolitano', 10)

def test_description_len():
    with pytest.raises(ValueError):
        team = Team('Metropolitano', 'c'*256)
