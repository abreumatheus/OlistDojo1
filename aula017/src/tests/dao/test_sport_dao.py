from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.sport_dao import SportDao
from src.models.sport import Sport
import pytest


class TestSportDao:
    def test_instance(self):
        sport_dao = SportDao()
        assert isinstance(sport_dao, SportDao)

    def test_save(self):
        sport = Sport('Um nome', 'Uma descrição')
        sport_saved = SportDao().save(sport)

        assert sport_saved.id_ is not None
        SportDao().delete(sport_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            sport_saved = SportDao().save('sport')

    def test_read_by_id(self):
        sport = Sport('Um nome', 'Uma descrição')
        sport_saved = SportDao().save(sport)
        sport_read = SportDao().read_by_id(sport_saved.id_)

        assert isinstance(sport_read, Sport)
        SportDao().delete(sport_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            sport_read = SportDao().read_by_id('sport_saved.id_')

    def test_read_all(self):
        sport_read = SportDao().read_all()

        assert isinstance(sport_read, list)

    def test_delete(self):
        sport = Sport('Um nome', 'Uma descrição')
        sport_saved = SportDao().save(sport)
        sport_read = SportDao().read_by_id(sport_saved.id_)
        SportDao().delete(sport_read)
        sport_read = SportDao().read_by_id(sport_saved.id_)

        assert sport_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            SportDao().delete('sport_read')
