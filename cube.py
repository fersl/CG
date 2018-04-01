from elements import *


class Cube(Obj):
    def __init__(self):
        self.vertices = {}
        self.faces = {}

        self.add_vertice(0.0, 0.0, 0.0)
        self.add_vertice(5.0, 0.0, 0.0)
        self.add_vertice(5.0, 5.0, 0.0)
        self.add_vertice(0.0, 5.0, 0.0)
        self.add_vertice(0.0, 0.0, -5.0)
        self.add_vertice(5.0, 0.0, -5.0)
        self.add_vertice(5.0, 5.0, -5.0)
        self.add_vertice(0.0, 5.0, -5.0)

        self.add_face(1, 2, 3)
        self.add_face(1, 3, 4)
        self.add_face(2, 6, 7)
        self.add_face(2, 7, 3)
        self.add_face(6, 5, 8)
        self.add_face(6, 8, 7)
        self.add_face(5, 1, 4)
        self.add_face(5, 4, 8)
        self.add_face(4, 3, 7)
        self.add_face(4, 7, 8)
        self.add_face(5, 6, 2)
        self.add_face(5, 2, 1)
