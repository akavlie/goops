from sqlalchemy import * 
from sqlalchemy.ext.declarative import declarative_base
from config import *

Base = declarative_base()

class Product(Base):
    __tablename__ = TABLE
    id = Column(Integer, primary_key=True)
    title = Column(TITLE_FIELD, String)
    description = Column(DESC_FIELD, String)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "<Product('%s')>" % self.title

    
