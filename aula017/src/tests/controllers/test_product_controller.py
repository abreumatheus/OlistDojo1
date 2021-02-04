import pytest

from src.controllers.base_controller import BaseController
from src.controllers.product_controller import ProductController
from src.models.product import Product


@pytest.fixture
def create_instance():
    product = ProductController()
    return product


def test_product_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, ProductController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()
    assert isinstance(result, list)


def test_read_by_id_with_invalid_id_should_raise_exception(create_instance):

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(71289379)
    assert str(exc.value) == 'Object not found in the database.'
