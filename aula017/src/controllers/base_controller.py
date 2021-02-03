from src.dao.base_dao import BaseDao
from src.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao: BaseDao):
        self.__dao = dao

    def read_all(self) -> list:
        return self.__dao.read_all()

    def read_by_id(self, id: int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        if result:
            return result
        raise Exception('Object not found in the database.')

    def create(self, model: BaseModel) -> BaseModel:
        return self.__dao.save(model)

    def update(self, model: BaseModel) -> BaseModel:
        self.read_by_id(model.id_)
        return self.__dao.save(model)

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
