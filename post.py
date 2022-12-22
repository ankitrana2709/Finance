import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("postgres://mxdbtvvr:aZWZQkZjukNsrrF2W85-kCV_-sLFIUgx@hansken.db.elephantsql.com/mxdbtvvr")) # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))