
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(String, primary_key=True)
    title = Column(String)
    publisher = Column(String)
    labels = Column(JSON)

def connect_to_database():
    engine = create_engine('mysql://user:password@host:port/library')
    Base.metadata.create_all(engine)
    return engine

def get_books():
    engine = connect_to_database()
    with engine.connect() as conn:
        books = conn.execute('SELECT * FROM books').fetchall()
    return books

def add_book(book_id, title, publisher, labels):
    engine = connect_to_database()
    with engine.connect() as conn:
        book = Book(book_id=book_id, title=title, publisher=publisher, labels=labels)
        conn.add(book)
        conn.commit()


engine = connect_to_database()
Base.metadata.create_all(engine)