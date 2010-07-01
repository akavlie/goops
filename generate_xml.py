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
                      .order_by(Product.id)
    xml = generate_template(products)

    xml_path = 'feed/' + XML_FILENAME 
    if os.path.exists(xml_path):
        today = date.today()
        date_string = '_' + str(today.month) + '-' + str(today.day)
        new_name = xml_path.split('.')[0] + date_string + '.xml'
        os.rename(xml_path, new_name)

    try:
        file = open(xml_path, 'w')
    except IOError:
        if not os.path.exists('feed'):
            os.mkdir('feed')
            file = open(xml_path, 'w')
    file.write(xml)
