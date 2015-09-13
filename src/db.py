import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = sqlalchemy.create_engine(os.environ.get('DATABASE_URL'))

Session = sessionmaker()
Session.configure(bind=engine)

