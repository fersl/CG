from basic_elements import *

class Pyramid(Obj):
	def __init__(self, id):
		self.id = id
		self.vertices = {}
		self.faces = {}
