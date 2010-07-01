import os, os.path
from datetime import date, datetime
from mako.template import Template
from connect import Session
from model import *

def generate_template(products):
    template = Template(filename='template.xml')
    return template.render(data=products)

if __name__ == '__main__':
    session = Session()
    products = session.query(Product) \
                      .filter_by(status='pending') \
                      .filter(Product.start_date < datetime.now()) \
                      .filter(Product.end_date > datetime.now()) \
                      .order_by(Product.id)[:10]
    xml = generate_template(products)

    if os.path.exists(XML_FILENAME):
        today = date.today()
        date_string = str(today.month) + '-' + str(today.day)
        new_name = 'feed/product_search-' + date_string + '.xml'
        os.rename('feed/product_search.xml', new_name)

    file = open(XML_FILENAME, 'w')
    file.write(xml)
