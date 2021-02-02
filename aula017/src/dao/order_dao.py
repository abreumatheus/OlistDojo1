from src.dao.base_dao import BaseDao
from src.models.order import Order


class OrderDao(BaseDao):
    def __init__(self):
        super().__init__(Order)
