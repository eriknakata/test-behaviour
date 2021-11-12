from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

db_user = 'admin'
db_password = 'admin'
db_host = 'localhost'
db_port = 5432
db_name = 'testing'

_database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name)

_engine = create_engine(_database_url, poolclass=StaticPool, echo=True)
_factory = sessionmaker(bind=_engine)
Session = scoped_session(sessionmaker(bind=_engine))