
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, String, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os




db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@db:3306/library")
connection = engine.connect()
base = declarative_base()

class transactions(base):
    __tablename__ = 'book'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(50))
    publisher = Column(String(50))
    labels = Column(JSON)

    def __init__(self, book_id, title, publisher, labels):
        self.book_id = book_id
        self.title = title
        self.publisher = publisher
        self.labels = labels 

base.metadata.create_all(engine)


