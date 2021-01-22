import sys
sys.path.append('.')

from backend.model.base_model import BaseModel
from backend.dao.category_dao import CategoryDao
from backend.controller.base_controller import BaseController


class CategoryController(BaseController):
    def __init__(self):
        self.dao = CategoryDao()
        super().__init__(self.dao)

# dao = CategoryController().read_all()
# print(dao[0].name)
