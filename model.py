from sqlalchemy import * 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config import *

Base = declarative_base()

class Product(Base):
    __tablename__ = TABLE
    id = Column(Integer, primary_key=True)
    title = Column(TITLE_FIELD, String)
    description = Column(DESC_FIELD, String)
    bids = relationship('Bid', order_by='Bid.id', backref='product')

    def _get_link(self, link=SITE+ITEM_PATH):
        return link % self.id
    def _get_image_link(self, link=SITE+IMAGE_PATH):
        return link % self.id

    link = property(_get_link)
    image_link = property(_get_image_link)

    def __repr__(self):
        return "<Product('%s')>" % self.title

class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(TABLE + '.id'))
    amount = Column('bid_price', String)

    def __repr__(self):
        return "<Bid('%s')>" % self.amount

    
