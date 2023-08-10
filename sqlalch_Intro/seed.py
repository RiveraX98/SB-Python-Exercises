from models import db, User, Post, Tag, PostTag
from app import app

db.session.rollback()
db.drop_all()
db.create_all()


test1 = User(first_name="Xavier", last_name='Rivera')
test2 = User(first_name="Ruben", last_name='Rivera')

test3 = Post(title="First Post", content="My first Post", user_id=1)
test4 = Post(title="Hello world", content="Hello", user_id=2)

tag1 = Tag(name="Good Vibez")
tag2 = Tag(name="TGIF")

rel1 = PostTag(post_id=1, tag_id=1)
rel2 = PostTag(post_id=2, tag_id=1)

db.session.add_all([test1, test2])
db.session.commit()
db.session.add_all([test3, test4])
db.session.commit()
db.session.add_all([tag1, tag2])
db.session.commit()
db.session.add_all([rel1, rel2])
db.session.commit()
