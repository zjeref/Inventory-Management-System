from sqlalchemy import Column, String, Integer,ForeignKey

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()




class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    quantity = Column(Integer)

    @property
    def informations(self):
        return {'id': self.id ,'item_id': self.item_id,
                'customer_id': self.customer_id, 'quantity': self.quantity}

