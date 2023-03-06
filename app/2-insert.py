
import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()

tr = db.transactions(0,'Green House', 'Joe Monter', '{"about" : {"gender": "action", "cool": true, "notes": "labeled"}}')

session.add(tr)
session.commit()

