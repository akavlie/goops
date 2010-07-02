import re
from sqlalchemy import * 
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
from config import *

def _strip_clean(text):
    """Strips slashes & html from text. """
    text = text.replace(r'\"', '"') \
               .replace(r"\'", "'") \
               .replace(r'&nbsp;', '') \
               .replace('&', '&amp;')
    return re.sub(r'<[^>]*?>', '', text)

Base = declarative_base()

class Product(Base):
    __tablename__ = TABLE
    id = Column(Integer, primary_key=True)
    status = Column('status', String)
    start_date = Column('start_date', DateTime)
    end_date = Column('end_date', DateTime)
    _raw_title = Column(TITLE_FIELD, String)
    _raw_description = Column(DESC_FIELD, String)
    bids = relationship('Bid', order_by='Bid.id', backref='product')

    def _get_link(self, link=SITE+ITEM_PATH):
        return link % self.id
    def _get_image_link(self, link=SITE+IMAGE_PATH):
        return link % self.id
    def _get_price(self):
        return max(self.bids).amount
    def _get_clean_description(self):
        return _strip_clean(self._raw_description)
    def _get_clean_title(self):
        return _strip_clean(self._raw_title)

    condition = CONDITION
    link = property(_get_link)
    image_link = property(_get_image_link)
    price = property(_get_price)
    title = property(_get_clean_title)
    description = property(_get_clean_description)

    def __repr__(self):
        return "<Product('%s')>" % self.title

class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(TABLE + '.id'))
    amount = Column('bid_price', String)

    def __repr__(self):
        return "<Bid('%s')>" % self.amount

    
