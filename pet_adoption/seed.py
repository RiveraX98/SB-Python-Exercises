from models import db, Pet
from app import app

db.session.rollback()
db.drop_all()
db.create_all()


test1 = Pet(name="Kurama", species="cat",
            photo_url="https://images.app.goo.gl/8rw6683LoyzXhwXS8", age=9, available=True)
test2 = Pet(name="Joker", species='dog',
            photo_url="https://images.app.goo.gl/2qYhhnFLKTDjx64C9", age=2, available=True)


db.session.add_all([test1, test2])
db.session.commit()
