# coding: utf-8

from mongoengine import connect
from app import app


if __name__ == '__main__':
	connect('localhost:27017')
	app.run(debug=True)
