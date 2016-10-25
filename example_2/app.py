# coding: utf-8

from difflib import SequenceMatcher, get_close_matches
from flask import Flask, jsonify, request


# objeto principal do flask
# responsável por criar a sua app
# o parametro __name__  serve para o flask
# saber o que tem na sua aplicação.
app = Flask(__name__)


@app.route('/', methods=('GET', ))
def home():
    return jsonify(
        {
            'API': [
                '/closest_word',
                '/proximity'
            ]
        }
    )


@app.route('/closest_word', methods=('GET', ))
def closest_word():
    possibilities = request.args.get('possibilities').split(',')
    word = request.args.get('word')
    try:
        closest_word = get_close_matches(word, possibilities, n=1)[0]
    except IndexError:
        closest_word = 'No matches'
    return jsonify({
        'closest_word': closest_word
    })


@app.route('/proximity', methods=('GET', ))
def proximity():
    word_a, word_b = request.args.get('word_a'), request.args.get('word_b')
    proximity = SequenceMatcher(a=word_a, b=word_b).ratio()
    return jsonify({
        'proximity': proximity
    })


if __name__ == '__main__':
    app.run(debug=True, port=8000)
