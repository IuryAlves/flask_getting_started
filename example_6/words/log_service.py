# coding: utf-8

import difflib
from .documents import ClosestWordLog, ProximityLog


def get_close_matches(word, possibilities):
    try:
        closest_word = difflib.get_close_matches(word, possibilities, n=1)[0]
    except IndexError:
        closest_word = 'No matches'
    ClosestWordLog(word=word, closest_word=closest_word).save()
    return closest_word


def get_proximity(word_a, word_b):
	proximity = difflib.SequenceMatcher(a=word_a, b=word_b).ratio()
	ProximityLog(word=word_a, word_b=word_b, proximity=proximity).save()
	return proximity
