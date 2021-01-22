import sys
sys.path.append('.')
from backend.model.category_model import Category

class TestCategoryModel:
    
    name = 'Isi'
    description = 'alguma coisa'

    def test_should_it(self):
        category = Category(self.name, self.description)
        assert category.name is self.name
        assert category.description is self.description

TestCategoryModel().test_should_it()

