# coding: utf-8


import json
import unittest
from app import app


class APITestCase(unittest.TestCase):

	def setUp(self):
		self.client = app.test_client()


	def test_closest_word(self):
		url = '/closest_word?possibilities={possibilities}&word={word}'.format(
			possibilities='ls, list, lst',
			word='lista'
			)

		response = self.client.get(url)
		data = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data, {'closest_word': ' list'})

	def test_proximity(self):
		url = '/proximity?word_a={word_a}&word_b={word_b}'.format(
			word_a='list',
			word_b='lista'
			)

		response = self.client.get(url)
		data = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data, {'proximity': 0.8888888888888888})


if __name__ == '__main__':
	unittest.main()
