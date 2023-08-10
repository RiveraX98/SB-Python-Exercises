from unittest import TestCase
from app import app
from models import db, User, Post, Tag, PostTag
from flask import Flask


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Test_users'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UsersTest(TestCase):

    def setUp(self):
        User.query.delete()
        Post.query.delete()
        user = User(first_name="John", last_name="Doe", image_url="Testurl")
        self.user = user

        post = Post(title="Helllo World", content="Testing post", user_id=1)
        self.post = post

        tag = Tag(name="TestTag")

        post_tag = PostTag(post_id=1, tag_id=1)

        db.session.add_all([user, post, tag, post_tag])
        db.session.commit()

    def tearDown(self):
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("All Users:", html)

    def test_create_user(self):
        with app.test_client() as client:
            d = {"first_name": "FirstName1",
                 "last_name": "LastName1", "image_url": "UrlTest1"}
            resp = client.post("/create_user", data=d,
                               follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1> FirstName1 LastName1 </h1>", html)

    def test_save_changes(self):
        with app.test_client() as client:
            d = {"first_name": "Jane"}
            resp = client.post(
                "/1", data=d,  follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Jane Doe</h1>", html)

    def test_add_post(self):
        with app.test_client() as client:
            d = {"title": "Test Post", "content": "My post", "user_id": 1}
            resp = client.post("/users/1/posts/new",
                               data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Test Post", html)

    def test_delete_user(self):
        with app.test_client() as client:

            resp = client.post("/1/delete_user",
                               follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>All Users:</h1>", html)

    def test_show_posts(self):
        with app.test_client() as client:
            resp = client.get("/posts/1/edit")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Edit Post</h1>", html)

    def test_save_post_edit(self):
        with app.test_client() as client:
            d = {"title": "Hello Edited", "content": "Post edited"}
            resp = client.post("/posts/1/edit", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Hello Edited</h1>", html)

    def test_delete_post(self):
        with app.test_client() as client:
            d = {"title": "Helllo World", "content": "Testing post", "user_id": 1}
            resp = client.post("/posts/1/delete", data=d,
                               follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("Hello World", html)

    def test_add_new_tag(self):
        with app.test_client() as client:
            d = {"new_tag": "TGIF"}
            resp = client.post("/tags/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("TGIF", html)

    def test_delete_tag(self):
        with app.test_client() as client:
            d = {"tag_id": 1}
            resp = client.post("/tag/1/delete", data=d,
                               follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("TestTag", html)

    def test_show_tag_form(self):
        with app.test_client() as client:
            resp = client.get("/tags/new")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Create New Tag", html)

    def test_edit_tag(self):
        with app.test_client() as client:
            d = {"name": "newTag", "tag_id": 1}
            resp = client.post("/tag/1/edit", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("newTag", html)
