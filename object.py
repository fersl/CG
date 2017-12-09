#define vertices, faces, e obj
import numpy as np

class Point(object):
	def __init__(self, point_id, coordinates_list):
		self.id = point_id
		self.coordinates = np.array(coordinates_list)


class Vector(object):
	def __init__(self, point1, point2):
		self.coordinates = point2.coordinates - point1.coordinates

	def normalize(self):
		norm = np.linalg.norm(self)
		self = self / norm
		self.coordinates[-1] = 0
		return self

	#def find


class Face:
	def __init__(self, face_id, points):
		self.id = face_id
		self.points

	def calculate_normal(self):
		v1 = Vector.__init__(self.points[0], self.points[2])
		v2 = Vector.__init__(self.points[1], self.points[2])
		n = np.cross(v1, v2)
		n = n.normalize()
		return n


class Object:
	def __init__(self, obj_id):
		self.id = obj_id
		self.vertices = []
		self.faces = []

	def add_vertices(self, x, y, z):
		vertice_id = len(self.vertices)+1
		vertice = Point.__init__(vertice_id, [x, y, z, 1])
		self.vertices.append(vertice)

	def add_faces(self, p1, p2, p3):
		face_id = len(self.faces)+1
		face = Face.__init__(face_id, [p1, p2, p3])
		self.faces.append(face)

	def apply_transformation(self, matrix):
		for p in self.vertices:
			p = np.dot(matrix, p)

	def aura_interception (self, ):

	def backface_culling(self, Pij):
		faces_list = []
		ray = Vector.__init__([0, 0, 0, 1], Pij).calculate_normal()
		for f in self.faces:
			v = f.calculate_normal
			if np.dot(v, ray) < 0
				faces_list.append(f)
		return faces_list