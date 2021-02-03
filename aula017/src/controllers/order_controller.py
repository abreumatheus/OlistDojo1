from src.controllers.base_controller import BaseController
from src.dao.order_dao import OrderDao


class OrderController(BaseController):
    def __init__(self):
        self.__dao = OrderDao()
        super().__init__(self.__dao)
