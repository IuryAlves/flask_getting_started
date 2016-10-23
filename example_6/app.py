# coding: utf-8

from flask import Flask
from mongoengine import connect
from words.api import words_blueprint

app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(words_blueprint, url_prefix='/words')
connect(host=app.config.get('DB_HOST'), port=app.config.get('DB_PORT'))
