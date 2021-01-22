import sys
sys.path.append('.')

from backend.controller.base_controller import BaseController
from backend.dao.product_dao import ProductDao


class ProductController(BaseController):
    def __init__(self):
        self.dao = ProductDao()
        super().__init__(self.dao)

dao = ProductController().read_all()
print(dao[0].name)
