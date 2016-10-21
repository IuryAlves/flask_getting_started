# coding: utf-8

from mongoengine import Document, fields


class ActivityLog(Document):
	meta = {
	'allow_inheritance': True
	}

	word = fields.StringField(required=True)

	def to_dict(self):
		return {
			'word': self.word
		}


class ClosestWordLog(ActivityLog):
	closest_word = fields.StringField(required=True)

	def to_dict(self):
		dic = super().to_dict()
		dic.update({
			'closest_word': self.closest_word
		})
		return dic
	

class ProximityLog(ActivityLog):
	proximity = fields.IntField(required=True)

	def to_dict(self):
		dic = super().to_dict()
		dic.update({
			'proximity': self.proximity
		})
		return dic
