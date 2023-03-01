
from sqlalchemy import create_engine, MetaData, Table, ForeignKey, ForeignKeyConstraint
from sqlalchemy import Column, String, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


uri = "mysql+pymysql://root:root@db/library"


engine = create_engine(uri, echo=True)
connection = engine.connect()

base = declarative_base()

class library(base):
    __tablename__ = 'transactions'

    book_id = Column(String, primary_key=True)
    title = Column(String)
    publisher = Column(String)
    labels = Column(JSON)

    def __init__(self, book_id, title, publisher, labels):
        self.book_id = book_id
        self.title = title
        self.publisher = publisher
        self.labels = labels 

base.metadata.create_all(engine)

