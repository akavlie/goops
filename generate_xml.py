from datetime import datetime
from mako.template import Template
from connect import Session
from model import *


def generate_template(products):
    template = Template(filename='template.xml')
    print template.render(data=products)

if __name__ == '__main__':
    session = Session()
    products = session.query(Product)
    products.filter_by(status='pending')
    products.filter(Product.start_date < datetime.now())
    products.filter(Product.end_date > datetime.now())
    products.order_by(Product.id)[:10]
    generate_template(products)
