from src.models.bet import Bet
import pytest

def test_id_customer_not_null():
    with pytest.raises(TypeError):
        bet = Bet(None, 1, 1, 10.0)

def test_id_match_not_null():
    with pytest.raises(TypeError):
        bet = Bet(1, None, 1, 10.0)

def test_id_team_sport_not_null():
    with pytest.raises(TypeError):
        bet = Bet(1, 1, None, 10.0)

def test_bet_value_not_null():
    with pytest.raises(TypeError):
        bet = Bet(1, 1, 0, None)

def test_bet_value_greater_than_0():
    with pytest.raises(ValueError):
        bet = Bet(1, 1, 0, -1.0)

def test_create_valid_bet():
    bet = Bet(1, 1, 0, 10.0)
    assert isinstance(bet, Bet)



        