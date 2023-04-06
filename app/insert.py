
import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()

tr1 = db.transactions(1,'Green House', 'Joe Monter', '{"about" : {"gender": "action", "cool": true, "notes": "labeled"}}')

session.add(tr1)
session.commit()

tr2 = db.transactions(2,'El camino', 'Daniil Zotl', '{"about" : {"gender": "documental", "cool": true, "notes": "labeled"}}')
tr3 = db.transactions(3,'London Bridge', 'Mario Mesa', '{"about" : {"gender": "drama", "cool": true, "notes": "labeled"}}')


session.add(tr2)
session.add(tr3)
session.commit()
