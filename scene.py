import numpy as np
from elements import *
from transformations import *
from cube import Cube


class Punctual_Light():
    def __init__(self, Id, Is, coords):
        self.diffuse = Id
        self.specular = Is
        self.position = np.array(coords)


class Camera():
    def __init__(self, position, look_at, avup):
        self.position = Point('camera', position[0], position[1], position[2])
        self.look_at = Point('look_at', look_at[0], look_at[1], look_at[2])
        self.avup = Point('avup', avup[0], avup[1], avup[2])

        self.i = []
        self.j = []
        self.k = []

        self.calculate_axis()

    def calculate_axis(self):
        z = Vector(self.look_at, self.position)
        k = z.normalize()

        vup = Vector(self.position, self.avup)
        vup = vup.normalize()

        x = cross_prod(vup, k)
        i = x.normalize()

        y = cross_prod(k, i)
        j = y.normalize()

        self.i = np.array(i.coordinates)
        self.j = np.array(j.coordinates)
        self.k = np.array(k.coordinates)

    def world_to_camera_matrix(self):
        coordinates = self.position.coordinates
        return np.array([
            [self.i[0], self.i[1], self.i[2], -np.dot(self.i, coordinates)],
            [self.j[0], self.j[1], self.j[2], -np.dot(self.j, coordinates)],
            [self.k[0], self.k[1], self.k[2], -np.dot(self.k, coordinates)],
            [0, 0, 0, 1]])

    def camera_to_world_matrix(self):
        return np.array([
            [self.i[0], self.j[0], self.k[0], self.position[0]],
            [self.i[1], self.j[1], self.k[1], self.position[1]],
            [self.i[2], self.j[2], self.k[2], self.position[2]],
            [0, 0, 0, 1]])


class Scene():
    def __init__(self):
        self.objects = []
        self.lights = []
        self.materials = {}
        self.ambient_light = [0.1, 0.1, 0.1]
        self.background_color = [0, 0, 0]

        self.load_materials()
        self.load_lights()
        self.load_objs()

    def load_materials(self):
        self.materials['royal_blue'] = Material(1, 65 / 255, 105 / 255, 55 / 255)
        # self.materials[] = Materials()

    def load_lights(self):
        coords = [4.0, 8.0, 8.0]
        Id = [0.5, 0.5, 0.5]
        Is = [0.5, 0.5, 0.5]
        self.lights.append(Punctual_Light(Id, Is, coords))

    def load_objs(self):
        obj1 = Cube()
        obj1.apply_material(self.materials['royal_blue'])
        m = translation_matrix([5, 3, 8])
        obj1.apply_transformation(m)
        self.objects.append(obj1)
