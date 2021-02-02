import sys
sys.path.append('.')
from src.models.team_sport import TeamSport
from src.models.team import Team
from src.models.sport import Sport
from src.models.product import Product
from src.models.order_product import OrderProduct
from src.models.order import Order
from src.models.match import Match
from src.models.customer import Customer
from src.models.bet import Bet
from src.dao.base_dao import BaseDao
import pytest
from datetime import datetime


@pytest.mark.parametrize('type_model', [
    Bet, Customer, Match,
    Order, OrderProduct, Product,
    Sport, Team, TeamSport
])
def test_instance(type_model):
    assert BaseDao(type_model), "Dao creation error!"


@pytest.mark.parametrize('type_model, attributs', [
    (Bet, {'id_customer': 1, 'id_match': 1,
           'id_team_sport': 1, 'bet_value': 1.}),
    (Match, {'id_team_sport_1': 1, 'id_team_sport_2': 2,
             'match_date': datetime.now(), 'score_team_1': 2,
             'score_team_2': 2})
])
def test_save(type_model, attributs):
    model = type_model(**attributs)
    base_dao = BaseDao(type_model)
    model = base_dao.save(model)
    assert model.id_ is not None, "Object not saved!"
    base_dao.delete(model)


@pytest.mark.parametrize('type_model', [
    Bet, Customer, Match,
    Order, OrderProduct, Product,
    Sport, Team, TeamSport
])
def test_read_all(type_model):
    base_dao = BaseDao(type_model)
    assert isinstance(base_dao.read_all(), list)


@pytest.mark.parametrize('type_model', [
    Bet, Customer, Match,
    Order, OrderProduct, Product,
    Sport, Team, TeamSport
])
def test_read_by_id(type_model):
    base_dao = BaseDao(type_model)
    id_ = 1
    assert isinstance(base_dao.read_by_id(id_), type_model)


@pytest.mark.parametrize('type_model, attributs', [
    (Bet, {'id_customer': 1, 'id_match': 1,
           'id_team_sport': 1, 'bet_value': 1.}),
    (Match, {'id_team_sport_1': 1, 'id_team_sport_2': 2,
             'match_date': datetime.now(), 'score_team_1': 2,
             'score_team_2': 2})
])
def test_delete(type_model, attributs):
    model = type_model(**attributs)
    base_dao = BaseDao(type_model)
    model = base_dao.save(model)
    id_ = model.id_
    base_dao.delete(model)
    with pytest.raises(Exception):
        test_read_by_id(id_)


@pytest.mark.parametrize('type_model, attributs', [
    (Bet, {'id_customer': 1, 'id_match': 1,
           'id_team_sport': 1, 'bet_value': 1.}),
    (Match, {'id_team_sport_1': 1, 'id_team_sport_2': 2,
             'match_date': datetime.now(), 'score_team_1': 2,
             'score_team_2': 2})
])
def test_update(type_model, attributs):
    model = type_model(**attributs)
    base_dao = BaseDao(type_model)
    model = base_dao.save(model)
    if isinstance(model, Bet):
        old_value = model.bet_value
        model.bet_value = float(3.14)
    elif isinstance(model, Match):
        old_date = model.match_date
        model.match_date = datetime.now()
    base_dao.save(model)
    if isinstance(model, Bet):
        assert old_value != model.bet_value
    elif isinstance(model, Match):
        assert old_date != model.match_date
    base_dao.delete(model)
