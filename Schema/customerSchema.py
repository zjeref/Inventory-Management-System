from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)

    @property
    def informations(self):
        return {'id':self.id,'Firstname': self.first_name ,'Lastname': self.last_name,
                'Phone': self.phone_number}


