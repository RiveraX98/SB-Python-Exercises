from unittest import TestCase
from app import app
from models import db, User
from flask import Flask


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Test_users'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UsersTest(TestCase):

    def setUp(self):
        User.query.delete()

    def tearDown(self):
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("All Users:", html)

    def test_create_user(self):
        with app.test_client as client:
            d = {"first_name": "FirstName1",
                 "last_name": "LastName1", "url": "UrlTest1"}
            resp = client.post("/create_user", data=d, follow_redirect=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1> FirstName1 LastName1 </h1>", html)

    def test_delete_user(self):
        with app.test_client as client:
            user = User(first_name="FirstName2",
                        last_name="LastName2", url="UrlTest2")
            db.session.add(user)
            db.session.commit()

            resp = client.post("/<int:user_id>/delete_user",
                               data=1, follow_redirect=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("<h1>FirstName2 LastName2")
