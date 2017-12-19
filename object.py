import numpy as np

class Point(object):
	def __init__(self, point_id, coordinates_list):
		self.id = point_id
		self.coordinates = np.array(coordinates_list)

	def to_vector(self):
		vector = Vector.__init__([0, 0, 0, 1], self.coordinates)
		return vector



class Vector(object):
	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2
		self.coordinates = point2.coordinates - point1.coordinates

	def normalize(self):
		norm = np.linalg.norm(self)
		self = self / norm
		self.coordinates[3] = 0
		return self



class Material(object):
	def __init__(self, k_a, k_d, k_s, m):
		self.m = m
		self.k_a = k_a
		self.k_d = k_d
		self.k_s = k_s



class Face(object):
	def __init__(self, face_id, points, material):
		self.id = face_id
		self.points = points
		#self.material = material 

	def calculate_normal(self):
		v1 = Vector.__init__(self.points[0], self.points[2])
		v2 = Vector.__init__(self.points[1], self.points[2])
		n = np.cross(v1, v2)
		n = n.normalize()
		return n

	def find_Pin(self, ray):
		n = self.calculate_normal()

		t = (np.dot(self.points[0], n)) / (np.dot(ray, n))
		Pin = ray * t 

		return [t, n, Pin]

	def contains(self, point):
		n = self.calculate_normal()

		w1 = Vector.__init__(point, self.points[0])
		w2 = Vector.__init__(point, self.points[1])
		w3 = Vector.__init__(point, self.points[2])

		n1 = np.cross(w1, w2)
		n2 = np.cross(w2, w3)
		n3 = np.cross(w3, w1)

		d1 = np.dot(n, w1)
		d2 = np.dot(n, w2)
		d3 = np.dot(n, w3)

		if d1 > 0:
			if d2 > 0:
				if d3 > 0:
					return True
		return False



class Object(object):
	def __init__(self, obj_id):
		self.id = obj_id
		self.vertices = {}
		self.faces = {}

	def add_vertice(self, x, y, z):
		vertice_id = len(self.vertices)+1
		vertice = Point.__init__(vertice_id, [x, y, z, 1])
		self.vertices[vertice_id] = vertice

	def add_face(self, p1, p2, p3, material):
		face_id = len(self.faces)+1
		face = Face.__init__(face_id, [p1, p2, p3], material)
		self.faces[face_id] = face

	def apply_transformation(self, matrix):
		for p in self.vertices:
			p = np.dot(matrix, p)

"""
### TO DO: 	adicionar material (ou cor?) as faces
	def build(self, file):
		material = "Default"

		with open(file) as file:
			for line in file:
				line.strip()
				data = line.split()

				if data[0] == '': continue

				elif data[0] == '#': continue

				elif data[0] == 'v':
					vertex = self.add_vertice (float(data[1]), float(data[2]), float(data[3]))

				#elif data[0] == 'usemtl':
				#	material = data[1]



				elif data[0] == 'f':
					self.add_face(self.vertices[data[1]], self.vertices[data[2]], self.vertices[data[3]], material)
#"""


	def aura_interception(self, Pij):
		x_max = -999999
		x_min = 999999

		y_max = -999999
		y_min = 999999

		z_max = -999999
		z_min = 999999

		for i in self.vertices:
			if x_max < i.coordinates[0]:
				x_max = i.coordinates[0]
			if y_max < i.coordinates[1]:
				y_max = i.coordinates[1]
			if z_max < i.coordinates[2]:
				z_max = i.coordinates[2]

			if x_min > i.coordinates[0]:
				x_min = i.coordinates[0]
			if y_min > i.coordinates[1]:
				y_min = i.coordinates[1]
			if z_min > i.coordinates[2]:
				z_min = i.coordinates[2]

		center = np.array([(x_max - x_min)/2, (y_max - y_min)/2, (z_max - z_min)/2])
		radius = (((x_max - center[0])**2) +
				   ((y_max - center[1])**2) +
				   ((z_max - center[2])**2)) ** 0.5

		A = np.dot(Pij, Pij)
		B = -2 * np.dot(Pij, center)
		C = (np.dot(center, center)) - (radius**2)

		delta = (B**2) - (4*A*C)

		if delta < 0:
			return False
		else:
			return True

	def backface_culling(self, Pij):
		faces_list = []
		ray = Pij.calculate_normal()
		for f in self.faces:
			v = f.calculate_normal
			if np.dot(v, ray) < 0:
				faces_list.append(f)
		return faces_list
