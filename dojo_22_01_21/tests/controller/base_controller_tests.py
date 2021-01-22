import sys
sys.path.append('.')
from backend.controller.base_controller import BaseController
from backend.dao.category_dao import CategoryDao
from backend.model.category_model import Category

categoryDao = CategoryDao()
base = BaseController(categoryDao)

assert isinstance(base.read_all(), list)
cat2 = base.read_all()
assert cat2 != None


