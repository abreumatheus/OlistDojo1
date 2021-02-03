import sys
sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.bet_dao import BetDao
from src.models.bet import Bet
import pytest


class TestbetDao:
    @pytest.fixture
    def create_instance(self):
        bet = Bet(1, 1, 1, 1.1)
        return bet

    def test_instance(self):
        bet_dao = BetDao()
        assert isinstance(bet_dao, BetDao)

    def test_save(self, create_instance):
        bet_saved = BetDao().save(create_instance)

        assert bet_saved.id_ is not None
        BetDao().delete(bet_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            BetDao().save('bet')

    def test_read_by_id(self, create_instance):
        bet_saved = BetDao().save(create_instance)
        bet_read = BetDao().read_by_id(bet_saved.id_)

        assert isinstance(bet_read, Bet)
        BetDao().delete(bet_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            BetDao().read_by_id('bet_saved.id_')

    def test_read_all(self):
        bet_read = BetDao().read_all()
        assert isinstance(bet_read, list)

    def test_delete(self, create_instance):
        bet_saved = BetDao().save(create_instance)
        bet_read = BetDao().read_by_id(bet_saved.id_)
        BetDao().delete(bet_read)
        bet_read = BetDao().read_by_id(bet_saved.id_)

        assert bet_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            BetDao().delete('bet_read')
