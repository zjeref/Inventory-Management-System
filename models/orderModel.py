from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///Inventory.db', echo = True)

Base = declarative_base()
Session = sessionmaker(bind=Engine)

from Schema.orderSchema import Order


class AbstractModel(ABC):

    def __init__(self):
        Base.metadata.create_all(Engine)
        self.session = Session()


class OrderModel(AbstractModel):

    def __init__(self):
        super(OrderModel, self).__init__()

    def new_order(self, **kwargs):
        self.session.add(Order(**kwargs))
        self.session.commit()

    def order_details(self, order_id):
        return self.session.query(Order).get(order_id)

    @property
    def getAllOrders(self):
        return self.session.query(Order).all()
