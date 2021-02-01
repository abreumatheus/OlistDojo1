from sqlalchemy.orm.relationships import foreign
from src.utils.validators import validate_not_empty, validate_type
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from src.models.base_model import BaseModel
from datetime import datetime
from sqlalchemy.orm import validates



class Order(BaseModel):
    __tablename__ = 'PUB_ORDER'
    order_date = Column('order_date', DateTime, nullable=False)
    id_customer = Column('id_customer', Integer,
                          ForeignKey('CUSTOMER.id'), nullable=False)
    customer = relationship('Customer', foreign_keys=[id_customer])
    total_value = Column('total_value', Float, default=0.0)                           


    def __init__(self, order_date: datetime, id_customer: int, total_value: float) -> None:
      self.order_date = order_date
      self.id_customer = id_customer
      self.total_value = total_value      
 

    @validates('order_date')
    def validate_order_date(self, key, order_date):
        return validate_type(order_date, datetime, key)    

    @validates('id_customer')
    def validate_id_customer(self, key, id_customer):
        return validate_type(id_customer, int, key)

    @validates('total_value')
    def validate_total_value(self, key, total_value):
        total = validate_type(total_value, float, key)
        return validate_be_greater_than_zero(total_value, key)         
