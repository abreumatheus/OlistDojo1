import sys
sys.path.append('.')

from sqlalchemy.orm import sessionmaker
from aula015.dao.base_dao import BaseDao
from aula015.models.category import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)


