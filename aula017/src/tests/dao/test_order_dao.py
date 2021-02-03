from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.order_dao import OrderDao
from src.models.order import Order
from datetime import datetime
import pytest


class TestOrderDao:
    @pytest.fixture
    def create_instance(self):
        order = Order(datetime.today(), 1, 10.2)
        return order

    def test_instance(self):
        order_dao = OrderDao()
        assert isinstance(order_dao, OrderDao)

    def test_save(self, create_instance):
        order_saved = OrderDao().save(create_instance)

        assert order_saved.id_ is not None
        OrderDao().delete(order_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            OrderDao().save('order')

    def test_read_by_id(self, create_instance):
        order_saved = OrderDao().save(create_instance)
        order_read = OrderDao().read_by_id(order_saved.id_)

        assert isinstance(order_read, Order)
        OrderDao().delete(order_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            OrderDao().read_by_id('order_saved.id_')

    def test_read_all(self):
        order_read = OrderDao().read_all()

        assert isinstance(order_read, list)
        assert all(isinstance(item, Order) for item in order_read)

    def test_delete(self, create_instance):
        dao = OrderDao()
        order_saved = dao.save(create_instance)
        order_read = dao.read_by_id(order_saved.id_)
        dao.delete(order_read)
        order_read = dao.read_by_id(order_saved.id_)

        assert order_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            OrderDao().delete('order_read')
