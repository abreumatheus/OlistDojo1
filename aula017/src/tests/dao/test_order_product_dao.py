from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.order_product_dao import OrderProductDao
from src.models.order_product import OrderProduct
import pytest


class TestOrderProductDao:
    @pytest.fixture
    def create_instance(self):
        order_product = OrderProduct(1, 1)
        return order_product

    def test_instance(self):
        order_product_dao = OrderProductDao()
        assert isinstance(order_product_dao, OrderProductDao)

    def test_save(self, create_instance):
        order_product_saved = OrderProductDao().save(create_instance)

        assert order_product_saved.id_ is not None
        OrderProductDao().delete(order_product_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            OrderProductDao().save('order')

    def test_read_by_id(self, create_instance):
        order_product_saved = OrderProductDao().save(create_instance)
        order_product_read = OrderProductDao().read_by_id(order_product_saved.id_)

        assert isinstance(order_product_read, OrderProduct)
        OrderProductDao().delete(order_product_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            OrderProductDao().read_by_id('order_product_saved.id_')

    def test_read_all(self):
        order_product_read = OrderProductDao().read_all()
        assert isinstance(order_product_read, list)
        assert all(isinstance(item, OrderProduct) for item in order_product_read)

    def test_delete(self, create_instance):
        dao = OrderProductDao()
        order_product_saved = dao.save(create_instance)
        order_product_read = dao.read_by_id(order_product_saved.id_)
        dao.delete(order_product_read)
        order_product_read = dao.read_by_id(order_product_saved.id_)

        assert order_product_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            OrderProductDao().delete('order_product_read')
