from aula015.models.base_model import BaseModel
from aula015.dao.session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BaseDao:
    def __init__(self, type_model):
        self.__type_model = type_model

    #insert, update
    def save(self, model:BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result

    def read_by_id(self, id:int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__type_model).filter_by(id=id).first()
        return result

    def delete(self, model:BaseModel)-> None:
        with Session() as session:
            session.delete(model)
            session.commit()
