from src.models.bet import Bet
import pytest

class TestBetDao:
    @pytest.fixture
    def create_instance(self):
        bet = Bet(1, 1, 0, 10.0)
        return bet
    def test_id_customer_not_null(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.id_customer = None

    def test_id_match_not_null(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.id_match = None

    def test_id_team_sport_not_null(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.id_team_sport = None

    def test_bet_value_not_null(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.bet_value = None

    def test_bet_value_greater_than_0(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.bet_value = -1.0

    def test_create_valid_bet(self, create_instance):
        assert isinstance(create_instance, Bet)



        