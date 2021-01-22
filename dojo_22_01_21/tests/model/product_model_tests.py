import sys
sys.path.append('.')
from backend.model.product_model import Product

class TestProductModel:
    
    name = 'Isi'
    description = 'alguma coisa'
    price = 4

    def test_should_it(self):
        product = Product(self.name, self.description, self.price)
        assert product.name is self.name
        assert product.description is self.description
        assert product.price is self.price
        assert isinstance(product, Product)

TestProductModel().test_should_it()

