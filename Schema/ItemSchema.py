from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    stock = Column(String)
    price = Column(String)

    @property
    def informations(self):
        return {'id': self.id ,'name': self.name,
                'description': self.description, 'stock': self.stock}

