from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class BoggleTests(TestCase):

    def setUp(self):

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        with self.client as client:
            self.client.get('/')
            self.assertIn('board', session)

    def test_invalid_word(self):
        with self.client as client:
            self.client.get('/')
            res = self.client.get("/check-word?word=momentaneousness")
            self.assertEqual(res.json['result'], 'not-on-board')

    def test_non_word(self):
        with self.client as client:
            self.client.get('/')
            res = self.client.get("/check-word?word=notaword")
            self.assertEqual(res.json['result'], 'not-word')
