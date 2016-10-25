# coding: utf-8

from flask import Blueprint, request, jsonify
from . import match_service

words_blueprint = Blueprint('word', __name__)


@words_blueprint.route('/', methods=('GET', ))
def home():
    return jsonify(
        {
            'API': [
                '/closest_word',
                '/proximity'
            ]
        }
    )


@words_blueprint.route('/closest_word', methods=('GET', ))
def closest_word():
    possibilities = request.args.get('possibilities').split(',')
    word = request.args.get('word')
    closest_word = match_service.get_close_matches(word, possibilities)
    return jsonify({
        'closest_word': closest_word
    })


@words_blueprint.route('/proximity', methods=('GET', ))
def proximity():
    word_a, word_b = request.args.get('word_a'), request.args.get('word_b')
    proximity = match_service.get_proximity(word_a, word_b)
    return jsonify({
        'proximity': proximity
    })
