from src.models.base_model import BaseModel
from src.dao.session import Session


class BaseDao:
    def __init__(self, type_model):
        self.__type_model = type_model
        
    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()
    
    def read_by_id(self, id_: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__type_model).filter_by(idgi=id_).first()
        return result
    
    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).order_by('id').all()
        return result
    
    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            result = session.delete(model)
            session.commit()
