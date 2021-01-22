from backend.model.base_model import BaseModel
from backend.dao.session import Session


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()
    
    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result

    def read_by_id(self, id: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__type_model).filter_by(id_=id).first()
        return result
    
    def delete(self, model:BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()