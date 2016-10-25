# coding: utf-8

from flask import Flask, jsonify

# objeto principal do flask
# responsável por criar a sua app
# o parametro __name__  serve para o flask
# saber o que tem na sua aplicação.

app = Flask(__name__)



@app.route('/')
def home():
    return jsonify({'message': 'Hello World !'})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
