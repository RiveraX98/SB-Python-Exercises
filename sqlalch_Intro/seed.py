from models import db, User, Post
from app import app

db.session.rollback()
db.drop_all()
db.create_all()


test1 = User(first_name="Xavier", last_name='Rivera')
test2 = User(first_name="Ruben", last_name='Rivera')

test3 = Post(title="First Post", content="My first Post", user_id=1)
test4 = Post(title="Hello world", content="Hello", user_id=2)

db.session.add_all([test1, test2])
db.session.commit()
db.session.add_all([test3, test4])
db.session.commit()
