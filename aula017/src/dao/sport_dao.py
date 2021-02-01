from src.models.sport import Sport
from src.dao.base_dao import BaseDao


class SportDao(BaseDao):
    def __init__(self):
        super().__init__(Sport)