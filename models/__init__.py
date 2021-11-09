from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.sql import func

from utils import engine

Base = declarative_base()


class Order(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    created = Column(TIMESTAMP, server_default=func.now())
    updated = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


Base.metadata.create_all(engine)
