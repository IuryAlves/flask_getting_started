# coding: utf-8

from flask import Flask
from mongoengine import connect
from words.api import words_blueprint

# objeto principal do flask
# responsável por criar a sua app
# o parametro __name__  serve para o flask
# saber o que tem na sua aplicação.
app = Flask(__name__)

app.config.from_object('settings')
app.register_blueprint(words_blueprint, url_prefix='/words')
connect(host=app.config.get('DB_HOST'), port=app.config.get('DB_PORT'))
