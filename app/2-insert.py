
import db 
from sqlalchemy.orm import sessionmakerx

class library(base):
    __tablename__ = 'transactions'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(30))
    publisher = Column(String(30))
    labels = Column(JSON)

    def __init__(self, book_id, title, publisher, labels):
        self.book_id = book_id
        self.title = title
        self.publisher = publisher
        self.labels = labels 

base.metadata.create_all(engine)

