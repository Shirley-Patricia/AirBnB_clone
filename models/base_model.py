#!/usr/bin/python3
"""

"""

from datetime import datetime

class BaseModel:

	def __init__(self, id, created_at, updated_at):
		self.id = id
		self.created_at = datetime.now().isoformat()
		self.updated_at = updated_at

	def __str__(self):
		"""should print [<class name>] (<self.id>) <self.__dict__>"""
		return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

	def save(self):
		"""updates the public instance attribute updated_at with the current datetime"""
		self.updated_at = datetime.now().isoformat()

	def to_dict(self):


