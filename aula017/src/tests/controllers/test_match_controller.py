import pytest

from src.controllers.base_controller import BaseController
from src.controllers.match_controller import MatchController
from src.models.match import Match
from datetime import datetime


@pytest.fixture
def create_instance():
    match = MatchController()
    return match

def test_match_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, MatchController)

def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)

def test_read_by_id_with_invalid_id_should_raise_exception(create_instance):
    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(999999)
    assert str(exc.value) == 'Object not found in the database.'

def test_invalid_relationship_exception(create_instance):
    with pytest.raises(Exception) as exc:
        create_instance.create(Match(1,9999999,datetime.today(),1,1))
    assert str(exc.value) == "Team sport 1 and Team sport 2 must exist."


