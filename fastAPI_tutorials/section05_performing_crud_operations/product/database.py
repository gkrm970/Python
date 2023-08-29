from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:root@10.168.170.87:3306/poc,pool_pre_ping=True"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@10.168.170.87:3306/poc, connect_args={'charset': 'utf8mb4'}"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/database_name"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

