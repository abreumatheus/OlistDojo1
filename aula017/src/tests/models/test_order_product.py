from src.models.order_product import OrderProduct
import pytest

@pytest.mark.parametrize('id_order, id_product', 
                        [('1', '2'),
                        ('1', 3),
                        (3, '2')
                        ])
def test_order_product_type(id_order, id_product):
    with pytest.raises(TypeError):
        order_product = OrderProduct(id_order, id_product)