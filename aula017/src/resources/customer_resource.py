from flask_restful import fields, marshal_with

from src.dao.customer_dao import CustomerDao
from src.models.customer import Customer
from src.resources.base_resource import BaseResource


class CustomerResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "name": fields.String,
        "num_doc": fields.String,
        "phone": fields.String
    }

    def __init__(self):
        self.__dao = CustomerDao()
        self.__model_type = Customer

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
