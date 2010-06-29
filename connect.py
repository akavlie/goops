from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import *
from model import *

# postgresql
#pg_db = create_engine('postgresql://scott:tiger@localhost/mydatabase')
# mysql
#mysql_db = create_engine('mysql://scott:tiger@localhost/foo')
# oracle - cx_oracle is the default driver
#oracle_db = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')
# sqlite://<nohostname>/<path>
# where <path> is relative:
    #sqlite_db = create_engine('sqlite:///foo.db')

mysql = 'mysql://%s:%s@%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_NAME) 

engine = create_engine(mysql)
Session = sessionmaker(bind=engine)


# For testing -- to remove
if __name__ == '__main__':
    session = Session()
    for item in session.query(Product).order_by(Product.id)[:10]:
        print item.title, ', ', item.description
        print 'Max Bid: ',
        print max(item.bids).amount
        #for bid in item.bids:
            #    print bid.amount ,
            

