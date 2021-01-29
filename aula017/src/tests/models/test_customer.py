from src.models.customer import Customer
import pytest


def test_customer_instance():
    customer = Customer('Teste', 'teste', 'teste')
    assert isinstance(customer, Customer)


def test_customer_name_empty():
    with pytest.raises(ValueError):
        customer = Customer('', 'num_doc', 'phone')


def test_customer_name_len():
    with pytest.raises(ValueError):
        customer = Customer('um nome bem grandrão' * 100, 'num_doc', 'phone')


def test_customer_name_int():
    with pytest.raises(TypeError):
        customer = Customer(100, 'descrição', 'phone')


def test_customer_num_doc_empty():
    with pytest.raises(ValueError):
        customer = Customer('Nome', '', 'phone')


def test_customer_num_doc_len():
    with pytest.raises(ValueError):
        customer = Customer('Nome', 'num_doc' * 500, 'phone')


def test_customer_num_doc_int():
    with pytest.raises(TypeError):
        customer = Customer('Nome', 10, 'phone')


def test_customer_phone_int():
    with pytest.raises(TypeError):
        customer = Customer('Nome', 'num_doc', 10)


def test_customer_phone_len():
    with pytest.raises(ValueError):
        customer = Customer('Nome', 'num_doc', 'phone'*100)