import sys
sys.path.append('.')

from backend.model.product_model import Product
from backend.dao.base_dao import BaseDao

class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)