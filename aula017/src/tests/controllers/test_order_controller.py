import pytest
import datetime

from src.controllers.base_controller import BaseController
from src.controllers.order_controller import OrderController
from src.controllers.customer_controller import CustomerController
from src.models.customer import Customer
from src.models.order import Order


class TestOrderController:
    @pytest.fixture
    def order_instance(self):
        controller = OrderController()
        return controller

    @pytest.fixture
    def customer_controller(self):
        return CustomerController()

    def test_order_controller_instance(self, order_instance):

        assert isinstance(order_instance, BaseController)
        assert isinstance(order_instance, OrderController)

    def test_read_all_should_return_list(self, order_instance):

        result = order_instance.read_all()

        assert isinstance(result, list)

    def test_create_order(self, order_instance, customer_controller):
        customer = Customer("Test Order", "123", "4199966633")
        customer = customer_controller.create(customer)
        date_time_str = 'Jun 28 2018 7:40AM'
        date = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
        id_customer = customer.id_
        value = 10.5
        order = Order(date, id_customer, value)

        result = order_instance.create(order)

        assert result.id_ is not None
        assert result.order_date == date
        assert result.id_customer == id_customer
        assert result.total_value == value

        order_instance.delete(result)
        customer_controller.delete(customer)

    def test_update_order(self, order_instance, customer_controller):
        customer = Customer("Test Order", "123", "4199966633")
        customer = customer_controller.create(customer)
        date_time_str = 'Jun 28 2018 7:40AM'
        date = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
        id_customer = customer.id_
        value = 10.5
        order = Order(date, id_customer, value)

        created = order_instance.create(order)

        new_date_time_str = 'Jun 28 2018 7:41AM'
        new_date = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
        new_value = 100.50
        created.order_date = new_date
        created.total_value = new_value

        result = order_instance.update(created)

        assert result.id_ is not None
        assert result.order_date == new_date
        assert result.id_customer == id_customer
        assert result.total_value == new_value

        order_instance.delete(result)
        customer_controller.delete(customer)

    def test_delete_order(self, order_instance, customer_controller):
        customer = Customer("Test Order", "123", "4199966633")
        customer = customer_controller.create(customer)
        date_time_str = 'Jun 28 2018 7:40AM'
        date = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
        id_customer = customer.id_
        value = 10.5
        order = Order(date, id_customer, value)

        created = order_instance.create(order)

        order_instance.delete(created)
        customer_controller.delete(customer)

        with pytest.raises(Exception) as exc:
            order_instance.read_by_id(created.id_)
            assert exc.value == "Object not found in the database."

    def test_read_by_id_should_return_order(self, order_instance, customer_controller):
        customer = Customer("Test Order", "123", "4199966633")
        customer = customer_controller.create(customer)
        date_time_str = 'Jun 28 2018 7:40AM'
        date = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')
        id_customer = customer.id_
        value = 10.5
        order = Order(date, id_customer, value)

        created = order_instance.create(order)
        result = order_instance.read_by_id(created.id_)

        assert isinstance(result, Order)
        assert result.id_ is not None
        assert result.order_date == date
        assert result.id_customer == id_customer
        assert result.total_value == value

        order_instance.delete(created)
        customer_controller.delete(customer)

    def test_read_by_id_with_invalid_id_should_raise_exception(self, order_instance):
        with pytest.raises(Exception) as exc:
            order_instance.read_by_id(71289379)
        assert str(exc.value) == "Object not found in the database."
