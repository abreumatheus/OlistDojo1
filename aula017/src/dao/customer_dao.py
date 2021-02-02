from src.dao.base_dao import BaseDao
from src.models.customer import Customer


class CustomerDao(BaseDao):
    def __init__(self):
        super().__init__(Customer)
