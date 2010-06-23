from sqlalchemy import create_engine
from config import *

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
