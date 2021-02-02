from src.dao.base_dao import BaseDao
from src.models.product import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
