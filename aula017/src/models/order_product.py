from sqlalchemy import Column, Integer
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import ForeignKey
from src.models.base_model import BaseModel
from src.utils.validators import validate_type
from src.models.product import Product


class OrderProduct(BaseModel):
    __tablename__ = 'ORDER_PRODUCT'

    id_order = Column('id_order', Integer, ForeignKey(
        'PUB_ORDER.id'), nullable=False)
    #pub_order = relationship('PubOrder', foreign_keys=[id_order])
    id_product = Column('id_product', Integer,
                        ForeignKey('PRODUCT.id'), nullable=False)
    product = relationship('Product', foreign_keys=[id_product])

    def __init__(self, id_order: int, id_product: int) -> None:
        self.id_order = id_order
        self.id_product = id_product

    @validates('id_order')
    def validate_id_order(self, key, id_order):
        return validate_type(id_order, int, key)

    @validates('id_product')
    def validate_id_product(self, key, id_product):
        return validate_type(id_product, int, key)
