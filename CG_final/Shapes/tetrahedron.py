from basic_elements import *
import math

class Tetrahedron(Obj):
	def __init__(self, id):
		self.id = id
		self.vertices = {}
		self.faces = {}

		self.add_vertice(0.0, 0.0, 0.0)
		self.add_vertice(1.0, 0.0, 0.0)
		self.add_vertice(1.5, 0.0, -1/sqrt(3))
		self.add_vertice(1.5, -1/sqrt(3), -1/(2*sqrt(3)))

		self.add_face(4, 1, 2)
		self.add_face(4, 2, 3)
		self.add_face(4, 3, 1)
		self.add_face(1, 2, 3)