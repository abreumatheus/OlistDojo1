from src.models.order import Order
from datetime import datetime
import pytest


@pytest.mark.parametrize('order_date, id_customer, total_value',
                        [('test', 1, 12.0),
                        (10, 2, 12.0),
                        (None, 2, 12), 
                        ])
def test_order_date_type(order_date, id_customer, total_value):
    with pytest.raises(TypeError):
        order_date = Order(order_date, id_customer, total_value)

@pytest.mark.parametrize('order_date, id_customer, total_value',
                        [(datetime.today(), 'test', 12.0),
                        (datetime.today(), None, 12.0),
                        (datetime.today(), 1.1, 12), 
                        ])
def test_id_customer_type(order_date, id_customer, total_value):
    with pytest.raises(TypeError):
        id_customer = Order(order_date, id_customer, total_value)

@pytest.mark.parametrize('order_date, id_customer, total_value',
                        [(datetime.today(), 10, 12),
                        (datetime.today(), 10, 'test'),
                        (datetime.today(), 2, None), 
                        ])
def test_total_value_type(order_date, id_customer, total_value):
    with pytest.raises(TypeError):
        total_value = Order(order_date, id_customer, total_value)

def test_total_value_be_greater_than_zero():
    with pytest.raises(ValueError):
        total_value = Order(datetime.today(), 1, -1.0)
