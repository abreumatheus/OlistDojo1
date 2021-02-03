import pytest

from src.controllers.base_controller import BaseController
from src.controllers.customer_controller import CustomerController
from src.models.customer import Customer


@pytest.fixture
def create_instance():
    controller = CustomerController()
    return controller


def test_customer_controller_instance(create_instance):
    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CustomerController)


def test_read_all_should_return_list(create_instance):
    result = create_instance.read_all()

    assert isinstance(result, list)


def test_create_customer(create_instance):
    name = 'Customer'
    num_doc = '000000000'
    phone = '41999999999'
    customer = Customer(name, num_doc, phone)

    result = create_instance.create(customer)

    assert result.id_ is not None
    assert result.name == name
    assert result.num_doc == num_doc
    assert result.phone == phone

    create_instance.delete(result)


def test_update_customer(create_instance):
    name = 'Customer'
    num_doc = '000000000'
    phone = '41999999999'
    customer = Customer(name, num_doc, phone)
    created = create_instance.create(customer)

    created.name = 'Customer 2'
    created.num_doc = '222222222'
    created.phone = '118888888'
    result = create_instance.update(created)

    assert result.id_ is not None
    assert result.name == 'Customer 2'
    assert result.num_doc == '222222222'
    assert result.phone == '118888888'

    create_instance.delete(result)


def test_delete_customer(create_instance):
    name = 'Customer'
    num_doc = '000000000'
    phone = '41999999999'
    customer = Customer(name, num_doc, phone)
    created = create_instance.create(customer)

    create_instance.delete(created)

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(created.id_)
        assert exc.value == 'Object not found in the database.'


def test_read_by_id_should_return_customer(create_instance):
    name = 'Customer'
    num_doc = '000000000'
    phone = '41999999999'
    customer = Customer(name, num_doc, phone)
    created = create_instance.create(customer)

    result = create_instance.read_by_id(created.id_)

    assert isinstance(result, Customer)
    assert result.name == name
    assert result.num_doc == num_doc
    assert result.phone == phone

    create_instance.delete(created)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = CustomerController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(71289379)
        assert str(exc.value) == 'Object not found in the database.'
