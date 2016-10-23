# coding: utf-8


import json
import unittest
from mongoengine import connect
from app import app
from db import ClosestWordLog, ProximityLog


class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        ClosestWordLog.drop_collection()
        ProximityLog.drop_collection()

    def test_closest_word(self):
        word = 'lista'
        url = '/closest_word?possibilities={possibilities}&word={word}'.format(
            possibilities='ls, list, lst',
            word=word
        )

        response = self.client.get(url)
        data = json.loads(response.data.decode())
        count_logs = ClosestWordLog.objects.filter(word=word).count()

        self.assertEqual(count_logs, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'closest_word': ' list'})

    def test_proximity(self):
        word_a = 'list'
        url = '/proximity?word_a={word_a}&word_b={word_b}'.format(
            word_a=word_a,
            word_b='lista'
        )

        response = self.client.get(url)
        data = json.loads(response.data.decode())
        count_logs = ProximityLog.objects.filter(word=word_a).count()

        self.assertEqual(count_logs, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'proximity': 0.8888888888888888})


if __name__ == '__main__':
    unittest.main()
