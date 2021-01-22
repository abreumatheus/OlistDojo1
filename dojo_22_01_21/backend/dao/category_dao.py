import sys
sys.path.append('.')

from backend.model.category_model import Category
from backend.dao.base_dao import BaseDao

class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
