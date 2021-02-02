from src.dao.base_dao import BaseDao
from src.models.order_product import OrderProduct


class OrderProductDao(BaseDao):
    def __init__(self):
        super().__init__(OrderProduct)
