import pytest

from src.controllers.base_controller import BaseController
from src.controllers.team_controller import TeamController
from src.models.team import Team


@pytest.fixture
def create_instance():
    controller = TeamController()
    return controller

def test_team_controller_instance(create_instance):

    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, TeamController)


def test_read_all_should_return_list(create_instance):

    result = create_instance.read_all()

    assert isinstance(result, list)


def test_create_team(create_instance):
    name = 'Team'
    description = 'Test'
    team = Team(name, description)

    result = create_instance.create(team)

    assert result.id_ is not None
    assert result.name == name
    assert result.description == description

    create_instance.delete(result)


def test_update_team(create_instance):
    name = 'Team'
    description = 'Test'
    team = Team(name, description)
    created = create_instance.create(team)

    created.name = 'Team 2'
    created.description = 'Test 2'
    result = create_instance.update(created)

    assert result.id_ is not None
    assert result.name == 'Team 2'
    assert result.description == 'Test 2'

    create_instance.delete(result)


def test_delete_team(create_instance):
    name = 'Team'
    description = 'Test'
    team = Team(name, description)
    created = create_instance.create(team)

    create_instance.delete(created)

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(created.id_)
        assert exc.value == 'Object not found in the database.'


def test_read_by_id_should_return_team(create_instance):
    name = 'Team'
    description = 'Test'
    team = Team(name, description)
    created = create_instance.create(team)

    result = create_instance.read_by_id(created.id_)

    assert isinstance(result, Team)
    assert result.name == name
    assert result.description == description

    create_instance.delete(created)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = TeamController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(71289379)
        assert exc.value == 'Object not found in the database.'
