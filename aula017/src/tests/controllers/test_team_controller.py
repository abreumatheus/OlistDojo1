import pytest

from src.controllers.base_controller import BaseController
from src.controllers.team_controller import TeamController
from src.models.team import Team


def test_team_controller_instance():
    controller = TeamController()

    assert isinstance(controller, BaseController)
    assert isinstance(controller, TeamController)


def test_read_all_should_return_list():
    controller = TeamController()

    result = controller.read_all()

    assert isinstance(result, list)


def test_create_team():
    controller = TeamController()
    name = 'Team'
    description = 'Test'
    team = Team(name, description)

    result = controller.create(team)

    assert result.id_ is not None
    assert result.name == name
    assert result.description == description

    controller.delete(result)


def test_update_team():
    controller = TeamController()
    name = 'Team'
    description = 'Test'
    team = Team(name, description)
    created = controller.create(team)

    created.name = 'Team 2'
    created.description = 'Test 2'
    result = controller.update(created)

    assert result.id_ is not None
    assert result.name == 'Team 2'
    assert result.description == 'Test 2'

    controller.delete(result)


def test_delete_team():
    controller = TeamController()
    name = 'Team'
    description = 'Test'
    team = Team(name, description)
    created = controller.create(team)

    controller.delete(created)

    with pytest.raises(Exception) as exc:
        controller.read_by_id(created.id_)
        assert exc.value == 'Object not found in the database.'


def test_read_by_id_should_return_team():
    controller = TeamController()
    name = 'Team'
    description = 'Test'
    team = Team(name, description)
    created = controller.create(team)

    result = controller.read_by_id(created.id_)

    assert isinstance(result, Team)
    assert result.name == name
    assert result.description == description

    controller.delete(created)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = TeamController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(71289379)
        assert exc.value == 'Object not found in the database.'
