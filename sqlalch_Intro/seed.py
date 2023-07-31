from models import db, User
from app import app

db.drop_all()
db.create_all()


test1 = User(first_name="Xavier", last_name='Rivera')
test2 = User(first_name="Ruben", last_name='Rivera')

db.session.add_all([test1,test2])
db.session.commit()
