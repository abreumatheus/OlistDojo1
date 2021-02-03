from sqlalchemy.orm.exc import UnmappedInstanceError
from datetime import datetime
from src.dao.match_dao import MatchDao
from src.models.match import Match
import pytest


class TestMatchDao:
    @pytest.fixture
    def create_instance(self):
        match = Match(1, 1, datetime.today(), 1, 1)
        return match

    def test_instance(self):
        match_dao = MatchDao()
        assert isinstance(match_dao, MatchDao)

    def test_save(self, create_instance):
        match_saved = MatchDao().save(create_instance)

        assert match_saved.id_ is not None
        MatchDao().delete(match_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            MatchDao().save('match')

    def test_read_by_id(self, create_instance):
        match_saved = MatchDao().save(create_instance)
        match_read = MatchDao().read_by_id(match_saved.id_)

        assert isinstance(match_read, Match)
        MatchDao().delete(match_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            MatchDao().read_by_id('match_saved.id_')

    def test_read_all(self):
        match_read = MatchDao().read_all()
        assert isinstance(match_read, list)

    def test_delete(self, create_instance):
        match_saved = MatchDao().save(create_instance)
        match_read = MatchDao().read_by_id(match_saved.id_)
        MatchDao().delete(match_read)
        match_read = MatchDao().read_by_id(match_saved.id_)

        assert match_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            MatchDao().delete('match_read')
