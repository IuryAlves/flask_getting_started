# coding: utf-8

from mongoengine import Document, fields


class ActivityLog(Document):
	meta = {
	'allow_inheritance': True
	}

	word = fields.StringField(required=True)


class ClosestWordLog(ActivityLog):
	closest_word = fields.StringField(required=True)
	

class ProximityLog(ActivityLog):
	proximity = fields.IntField(required=True)
