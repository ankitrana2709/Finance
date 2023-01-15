"""
engine = create_engine(os.getenv("postgres://mxdbtvvr:aZWZQkZjukNsrrF2W85-kCV_-sLFIUgx@hansken.db.elephantsql.com/mxdbtvvr")) # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))
try:
    with 
CREATE TABLE transactions (
	trans_id SERIAL PRIMARY KEY NOT NULL,
	user_id INTEGER NOT NULL,
	comp_id INTEGER NOT NULL,
	shares INTEGER NOT NULL,
	price REAL NOT NULL,
	time DATETIME NOT NULL
)

-- Users Table
CREATE TABLE users (
	user_id Serial PRIMARY KEY NOT NULL,
	username TEXT NOT NULL,
	hash TEXT NOT NULL,
	cash NUMERIC NOT NULL DEFAULT 10000.00
)"""