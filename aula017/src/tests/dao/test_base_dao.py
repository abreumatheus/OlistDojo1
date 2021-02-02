import sys
sys.path.append('.')
from datetime import datetime
import pytest
from src.dao.base_dao import BaseDao
from src.models.bet import Bet
from src.models.customer import Customer
from src.models.match import Match
from src.models.order import Order
from src.models.order_product import OrderProduct
from src.models.product import Product
from src.models.sport import Sport
from src.models.team import Team
from src.models.team_sport import TeamSport
from src.dao.session import Session



@pytest.mark.parametrize('type_model', [
                                            Bet, Customer, Match, 
                                            Order, OrderProduct, Product, 
                                            Sport, Team, TeamSport
                                        ])
def test_instance(type_model):
    assert BaseDao(type_model), "Dao creation error!"

@pytest.mark.parametrize('type_model, attributes', [
                                                        (Bet, {'id_customer': 1, 'id_match': 1, 
                                                        'id_team_sport': 1, 'bet_value': 1}),
                                                        (Match, {'id_team_sport_1': 1, 'id_team_sport_2': 2, 
                                                        'match_date': datetime.now(), 'score_team_1': 2, 
                                                        'score_team_2': 2})
                                                    ])
def test_save(type_model, attributes):
    model = type_model(**attributes.values())
    base_dao = BaseDao(type_model)
    base_dao.save(model)
