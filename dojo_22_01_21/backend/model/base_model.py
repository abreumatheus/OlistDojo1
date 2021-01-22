from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    
    id_ = Column( 'id', Integer, primary_key=True )


