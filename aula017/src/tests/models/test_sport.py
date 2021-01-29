from src.models.sport import Sport
import pytest


def test_sport_instance():
    sport = Sport('Esporte1', 'Esporte legal')

    assert isinstance(sport, Sport)


def test_sport_name_empty():
    with pytest.raises(ValueError):
        sport = Sport('', 'descrição')


def test_sport_name_len():
    with pytest.raises(ValueError):
        sport = Sport('um nome bem grandrão' * 100, 'descrição')


def test_sport_name_int():
    with pytest.raises(TypeError):
        sport = Sport(100, 'descrição')


def test_sport_description_len():
    with pytest.raises(ValueError):
        sport = Sport('Nome', 'descrição' * 500)


def test_sport_description_int():
    with pytest.raises(TypeError):
        sport = Sport('Nome', 10)
