from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///Inventory.db', echo = True)

Base = declarative_base()
Session = sessionmaker(bind=Engine)

from Schema.ItemSchema import Items


class AbstractModel(ABC):

    def __init__(self):
        Base.metadata.create_all(Engine)
        self.session = Session()


class ItemsModel(AbstractModel):

    def __init__(self):
        super(ItemsModel, self).__init__()

    def insert_items(self, data):
        
        self.session.add(Items(id=data[1], name=data[2],description=data[3],stock=data[4]))
        self.session.commit()

    def delete_items(self, item_id):
        self.session.delete(
            self.session.query(Items).filter(Items.id == item_id).first()
        )
        self.session.commit()

    def update_items(self, item_id, **kwargs):
        self.session.query(Items).filter(Items.id == item_id).update(kwargs)
        self.session.commit()

    def item_details(self, item_id):
        return self.session.query(Items).get(item_id)

    @property
    def getAllItems(self):
        return self.session.query(Items).all()
