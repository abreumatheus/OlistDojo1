import pytest

from src.controllers.base_controller import BaseController
from src.controllers.sport_controller import SportController
from src.models.sport import Sport

@pytest.fixture
def create_instance():
    sport = SportController()
    return sport


def test_sport_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, SportController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = SportController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(71289379)
    assert str(exc.value) == 'Object not found in the database.'
