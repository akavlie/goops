from mako.template import Template
from connect import Session
from model import *


def generate_template(products):
    template = Template(filename='template.xml')
    print template.render(data=products)

if __name__ == '__main__':
    session = Session()
    products = session.query(Product).order_by(Product.id)[:10]
    generate_template(products)
