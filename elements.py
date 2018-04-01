import numpy as np


class Material():
    def __init__(self, m, r, g, b):
        self.m = m
        self.k_a = [r, g, b]
        self.k_d = [r, g, b]
        self.k_s = [r, g, b]


class Point():
    def __init__(self, id, x, y, z):
        self.id = id
        self.coordinates = np.array([x, y, z, 1])
        self.material = None

    def to_vector(self):
        p0 = Point('p0', 0, 0, 0)
        return Vector(p0, self)

    def apply_material(self, obj):
        f = self.get_face(obj)
        self.material = f.material

    def get_face(self, obj):
        for face in obj.faces.values():
            if face.contains(self):
                return face


class Vector():
    def __init__(self, p1, p2):
        # receives 2 Points
        self.point1 = p1.coordinates
        self.point2 = p2.coordinates
        self.coordinates = np.array(self.point2 - self.point1)

    def normalize(self):
        norm = np.linalg.norm(self.coordinates)
        self.coordinates[0] = self.coordinates[0] / norm
        self.coordinates[1] = self.coordinates[1] / norm
        self.coordinates[2] = self.coordinates[2] / norm
        self.coordinates[3] = self.coordinates[3] / norm
        return self
        # returns a Vector


class Face():
    def __init__(self, id, p1, p2, p3):
        self.id = id
        self.points = [p1, p2, p3]
        self.material = None

    def get_normal(self):
        v1 = Vector(self.points[0], self.points[1])
        v2 = Vector(self.points[0], self.points[2])
        n = cross_prod(v1, v2)
        return n.normalize()

    def apply_material(self, mat):
        self.material = mat

    #IMPLEMENTAR
    def get_Pin(self, ray):
        n = self.get_normal()
        v = self.points[0]

        t = np.dot(v.coordinates, n.coordinates) / np.dot(ray.coordinates, n.coordinates)
        x = ray.coordinates[0] * t
        y = ray.coordinates[1] * t
        z = ray.coordinates[2] * t

        return Point('pin', x, y, z)

    def contains(self, point):
        n = self.get_normal()

        w1 = Vector(point, self.points[0])
        w2 = Vector(point, self.points[1])
        w3 = Vector(point, self.points[2])

        n1 = cross_prod(w1, w2)
        n2 = cross_prod(w2, w3)
        n3 = cross_prod(w3, w1)

        d1 = np.dot(n1.coordinates, n.coordinates)
        d2 = np.dot(n2.coordinates, n.coordinates)
        d3 = np.dot(n3.coordinates, n.coordinates)

        if d1 > 0:
            if d2 > 0:
                if d3 > 0:
                    return True
        return False


class Obj():
    def __init__(self):
        self.vertices = {}
        self.faces = {}

    def add_vertice(self, x, y, z):
        vertice_id = len(self.vertices) + 1
        vertice = Point(vertice_id, x, y, z)
        self.vertices[vertice_id] = vertice

    def add_face(self, p1, p2, p3):
        face_id = len(self.faces) + 1
        face = Face(face_id, self.vertices[p1],
                    self.vertices[p2], self.vertices[p3])
        self.faces[face_id] = face

    def apply_transformation(self, matrix):
        for v in self.vertices.values():
            v = np.dot(matrix, v.coordinates)

    def apply_material(self, mat):
        for f in self.faces.values():
            f.apply_material(mat)

    def intercepts(self, ray):
        # ray é um vetor
        if self.intercepts_aura(ray):
            faces = self.backface_culling(ray)
            for face in faces:
                Pin = face.get_Pin(ray)
                if Pin != None:
                    if face.contains(Pin):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

    def intercepts_aura(self, ray):
        x_max = -999999
        x_min = 999999

        y_max = -999999
        y_min = 999999

        z_max = -999999
        z_min = 999999

        for v in self.vertices.values():
            if x_max < v.coordinates[0]:
                x_max = v.coordinates[0]
            if y_max < v.coordinates[1]:
                y_max = v.coordinates[1]
            if z_max < v.coordinates[2]:
                z_max = v.coordinates[2]

            if x_min > v.coordinates[0]:
                x_min = v.coordinates[0]
            if y_min > v.coordinates[1]:
                y_min = v.coordinates[1]
            if z_min > v.coordinates[2]:
                z_min = v.coordinates[2]

        center = np.array([(x_max - x_min) / 2,
                           (y_max - y_min) / 2,
                           (z_max - z_min) / 2])
        X = (x_max - center[0]) ** 2
        Y = (y_max - center[1]) ** 2
        Z = (z_max - center[2]) ** 2
        radius = (X + Y + Z) ** 0.5

        ray_coordinates = np.array([ray.coordinates[0], ray.coordinates[1], ray.coordinates[2]])
        A = np.dot(ray_coordinates, ray_coordinates)
        B = -2 * np.dot(ray_coordinates, center)
        C = np.dot(center, center) - (radius ** 2)

        delta = (B**2) - (4 * A * C)

        if delta < 0:
            return False
        else:
            return True

    def backface_culling(self, ray):
        # ray is a vector
        r = ray.coordinates
        faces_list = []
        for f in self.faces.values():
            n = f.get_normal()
            n = n.coordinates
            if np.dot(n, r) < 0:
                faces_list.append(f)
        return faces_list


def cross_prod(v1, v2):
    vector1 = np.array([v1.coordinates[0], v1.coordinates[1], v1.coordinates[2]])
    vector2 = np.array([v2.coordinates[0], v2.coordinates[1], v2.coordinates[2]])
    result = np.cross(vector1, vector2)
    p1 = Point('p', result[0], result[1], result[2])
    p0 = Point('p0', 0, 0, 0)
    return Vector(p0, p1)
