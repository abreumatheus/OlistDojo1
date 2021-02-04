from typing import Type

from flask import request
from flask_restful import Resource

from src.dao.base_dao import BaseDao


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type):
        self.__dao = dao
        self.__model_type = model_type

    def get(self, id=None):
        if id:
            return self.__dao.read_by_id(id)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        item = self.__model_type(**data)
        self.__dao.save(item)

        return item, 201

    def put(self, id):
        data = request.json

        if data['id_'] == id:
            item = self.__dao.read_by_id(id)
            # updated_item = item(**data)
            # item.update(updated_item)

            for key, value in data.items():
                setattr(item, key, value)

            return self.__dao.save(item)

        return None, 404

    def delete(self, id):
        item = self.__dao.read_by_id(id)
        self.__dao.delete(item)
        return None, 204
