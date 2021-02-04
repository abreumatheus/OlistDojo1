from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from src.models.base_model import BaseModel
from src.utils.validators import validate_type, validate_not_empty, validate_len


class Customer(BaseModel):
    __tablename__ = 'CUSTOMER'
    name = Column('name', String(length=100), nullable=False)
    num_doc = Column('num_doc', String(length=50), nullable=False)
    phone = Column('phone', String(length=20), nullable=True)

    def __init__(self, name: str, num_doc: str, phone: str) -> None:
        self.name = name
        self.num_doc = num_doc
        self.phone = phone

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        return validate_len(name, 100, key)

    @validates('num_doc')
    def validate_num_doc(self, key, num_doc):
        num_doc = validate_type(num_doc, str, key)
        num_doc = validate_not_empty(num_doc, key)
        return validate_len(num_doc, 50, key)

    @validates('phone')
    def validate_phone(self, key, phone):
        phone = validate_type(phone, str, key)
        return validate_len(phone, 20, key)
