from src.controllers.base_controller import BaseController
from src.dao.customer_dao import CustomerDao


class CustomerController(BaseController):
    def __init__(self):
        self.__dao = CustomerDao()
        super().__init__(self.__dao)
