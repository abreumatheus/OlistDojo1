from src.models.product import Product
import pytest

@pytest.mark.parametrize('name,price,description',
                        [('nome', 6.6, None),('nome aleatorio', 3.4, 'descricao')])
def test_product_instance(name, price, description):
    product = Product(name, price, description)

    assert isinstance(product, Product)
    assert product.name == name
    assert product.price == price
    assert product.description == description


def test_product_name_empty():
    with pytest.raises(ValueError):
        product = Product('', 3.4, 'descricao')


def test_product_name_len():
    with pytest.raises(ValueError):
        product = Product('nome aleatorio'*100, 3.4, 'descricao')


def test_product_name_int():
    with pytest.raises(TypeError):
        product = Product(10, 3.4, 'descricao')


def test_product_description_len():
    with pytest.raises(ValueError):
        product = Product('nome aleatorio', 3.4, 'descricao'*300)


def test_product_description_int():
    with pytest.raises(TypeError):
        product = Product('nome aleatorio', 3.4, 123)


def test_product_price_zero():
    with pytest.raises(ValueError):
        product = Product('nome aleatorio', 0.0, 'descricao')


def test_product_price_not_float():
    with pytest.raises(TypeError):
        product = Product('nome aleatorio', '', 'descricao')
