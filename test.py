from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    # def setUp(self):
    #     # boggle_game = Boggle()
    #     # session['board'] = boggle_game.make_board()
    #     # session['guesses'] = []
    #     return super().setUp()

    def test_game_run(self):
        with app.test_client() as client:
            resp = client.get('/')
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn('<h1>Boggle</h1>', html)

    def test_answer_attempt(self):
        with app.test_client() as client:
            client.get('/')
            resp = client.post('/answer_attempt', json={'attempt': 'hi'})
            self.assertIn('result', resp.get_data(as_text=True))
