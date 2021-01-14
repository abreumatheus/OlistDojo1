import sys
sys.path.append('.')

from aula014.controllers.base_controller import BaseController
from aula014.dao.category_dao import CategoryDao


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao)


