from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///Inventory.db', echo = True)

Base = declarative_base()
Session = sessionmaker(bind=Engine)

from Schema.customerSchema import Customer



class AbstractModel(ABC):

    def __init__(self):
        Base.metadata.create_all(Engine)
        self.session = Session()


class CustomerModel(AbstractModel):

    def __init__(self):
        super(CustomerModel, self).__init__()

    def new_user(self, **kwargs):
        self.session.add(Customer(**kwargs))
        self.session.commit()

    def user_details(self, customer_id):
        return self.session.query(Customer).get(customer_id)

    @property
    def getAllCustomers(self):
        return self.session.query(Customer).all()
