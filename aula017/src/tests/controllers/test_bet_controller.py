import pytest

from src.controllers.base_controller import BaseController
from src.controllers.bet_controller import BetController
from src.models.bet import Bet


@pytest.fixture
def create_instance():
    bet = BetController()
    return bet


def test_bet_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, BetController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)


def test_read_by_id_with_invalid_id_should_raise_exception(create_instance):

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(71289379)
    assert str(exc.value) == 'Object not found in the database.'
