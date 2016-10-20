# coding: utf-8

from difflib import SequenceMatcher, get_close_matches
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=('GET', ))
def home():
    return jsonify(
        {
            'API': [
                '/close_match',
                '/proximity'
            ]
        }
    )


@app.route('/close_match', methods=('GET', ))
def close_match():
    possibilities = request.args.get('possibilities').split(',')
    word = request.args.get('word')
    return jsonify({
        'result': get_close_matches(word, possibilities, n=1)
    })


@app.route('/proximity', methods=('GET', ))
def proximity():
    word_a, word_b = request.args.get('word_a'), request.args.get('word_b')
    return jsonify({
        'result': SequenceMatcher(a=word_a, b=word_b).ratio()
    })


if __name__ == '__main__':
    app.run(debug=True)
