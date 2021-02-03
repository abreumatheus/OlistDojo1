from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.product_dao import ProductDao
from src.models.product import Product
import pytest


class TestProductDao:
    @pytest.fixture
    def create_instance(self):
        product = Product('Um nome', 5.99, 'Uma descrição')
        return product

    def test_instance(self):
        product_dao = ProductDao()
        assert isinstance(product_dao, ProductDao)

    def test_save(self, create_instance):
        product_saved = ProductDao().save(create_instance)

        assert product_saved.id_ is not None
        ProductDao().delete(product_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            product_saved = ProductDao().save('product')

    def test_read_by_id(self, create_instance):
        product_saved = ProductDao().save(create_instance)
        product_read = ProductDao().read_by_id(product_saved.id_)

        assert isinstance(product_read, Product)
        ProductDao().delete(product_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            product_read = ProductDao().read_by_id('product_saved.id_')

    def test_read_all(self):
        product_read = ProductDao().read_all()

        assert isinstance(product_read, list)

    def test_delete(self, create_instance):
        product_saved = ProductDao().save(create_instance)
        product_read = ProductDao().read_by_id(product_saved.id_)
        ProductDao().delete(product_read)
        product_read = ProductDao().read_by_id(product_saved.id_)

        assert product_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            ProductDao().delete('product_read')
