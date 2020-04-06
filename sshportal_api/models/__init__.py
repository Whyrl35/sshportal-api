from sqlalchemy import MetaData
from sshportal_api import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# FIXME: https://github.com/blakev/Flask-WhooshAlchemy3
# need to index movie on title, seen, is_series

if app.config['DATABASE']['type'] == 'sqlite':
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE']['sqlite']['uri']
elif app.config['DATABASE']['type'] == 'mysql':
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{username}:{password}@{host}/{database}".format(
        username=app.config['DATABASE']['mysql']['user'],
        password=app.config['DATABASE']['mysql']['password'],
        host=app.config['DATABASE']['mysql']['host'],
        database=app.config['DATABASE']['mysql']['database'],
    )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

metadata = MetaData(
  naming_convention={
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'idx_%(table_name)s_%(column_0_name)s',
    'uq': 'uix_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    }
)

db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


from .acls import *  # noqa
from .events import *  # noqa
from .hostgroups import *  # noqa
from .hosts import *  # noqa
from .sessions import *  # noqa
from .settings import *  # noqa
from .sshkeys import *  # noqa
from .usergroups import *  # noqa
from .userkeys import *  # noqa
from .userroles import *  # noqa
from .users import *  # noqa
