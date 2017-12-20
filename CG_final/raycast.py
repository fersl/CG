import numpy as np
from basic_elements import *


class Camera(object):
    def __init__(position, look_at, avup):
        self.position = Point.__init__("camera", position)
        self.look_at = Point.__init__("look_at", look_at)
        self.avup = Point.__init__("avup", avup)
        self.i = []
        self.j = []
        self.k = []

    def calculate_axis():
        z = Vector.__init__(look_at, position)
        self.k = z.normalize()
        vup = Vector.__init__(position, avup)
        vup = vup.normalize()
        x = np.cross(vup, self.k)
        self.i = x.normalize
        y = n.cross(self.k, self.i)
        self.j = y.normalize
        return [self.i, self.j, self.k]

    def world_to_camera_matrix():
        return np.array([
            [self.i[0], self.i[1], self.i[2], -np.dot(self.i, self.position)],
            [self.j[0], self.j[1], self.j[2], -
             np.dot(self.j, self.position)],
            [self.k[0], self.k[1], self.k[2], -
             np.dot(self.k, self.position)],
            [0, 0, 0, 1]])

    def camera_to_world_matrix():
        return np.array([
            [self.i[0], self.j[0], self.k[0], self.position[0]],
            [self.i[1], self.j[1],
             self.k[1], self.position[1]],
            [self.i[2], self.j[2],
             self.k[2], self.position[2]],
            [0, 0, 0, 1]])


class Punctual_Light(object):
    def __init__(self, Id, Is, coordinates):
        self.diffuse = Id
        self.specular = Is
        self.coordinates = coordinates


class Spot_light(object):
    def __init__(self, Id, Is, coordinates, angle):
        self.diffuse = Id
        self.specular = Is
        self.coordinates = coordinates
        # self.angle
        # self.normal


class Raycast(object):
    def __init__(self):
        self.ambient_light = [0.1, 0.1, 0.1]

    def apply_mwc(self, mwc, scene):
        for obj in scene:
            obj.apply_transformation(mwc)

    def apply_mcw(self, mcw, scene):
        for obj in scene:
            obj.apply_transformation(mcw)

    def build_window(params):
        points_window = np.matlib.zeros(n, m)

        d = params[0]
        n = params[1]
        m = params[2]
        W = params[3]
        H = params[4]

        deltaX = W / m
        deltaY = H / n

        for i in range(n):
            x = -(W / 2) + (deltaX / 2) + j * deltaX

            for j in range(m):
                y = (H / 2) - (deltaY / 2) - i * deltaY

                points_window[i, j] = [x, y, -d]

        return points_window

    def intersection_window(self, window, scene):
        # intersection_window = np.matlib.zeros(n, m)

        for pixel in window.flat:
            ray = pixel.to_vector()
            ray = ray.normalize()
            # [t, normal_of_face, Pin_coords, material]
            intersection = [999999, None, None, None]

            for obj in scene:
                if obj.aura_interception(pixel):
                    visible_faces = obj.backface_culling(pixel)

                    for face in visible_faces:
                        aux = face.find_Pin(ray)

                        if face.contains(aux[2]):
                            if aux[0] < intersection[0]:
                                intersection = aux
            # [point, normal_vector, material]
            pixel = [intersection[2], intersection[1], intersection[3]]

        return window

    def color_window(self, points_window, scene):
        # light = scene.light
        # color_window = np.matlib.zeros(n, m)

        for pixel in points_window.flat:
            v = pixel.to_vector()
            v = v.normalize()
            n = pixel[1]
            color = []

            m = pixel[3].m
            k_a = pixel[3].k_a
            k_d = pixel[3].k_d
            k_s = pixel[3].k_s

            Ia = [k_a[0] * scene.ambient_light[0],
                  k_a[1] * scene.ambient_light[1],
                  k_a[2] * scene.ambient_light[2]]

            color = color + Ia

            for light in scene.lights.values():
                l = Vector(pixel, light.coordinates)
                l = l.normalize()
                r = ((2 * np.dot(n, l)) * n) - l
                r = r.normalize()

                interception = False
                for obj in scene:
                	while not interception:
	                	if obj.aura_interception(l):
	                    	visible_faces = obj.backface_culling(l)

	                    	for face in visible_faces:
	                        	aux = face.find_Pin(l)

	                        	if face.contains(aux[2]):
	                        		interception = True
	                        		break

	            if not interception: 
	                Id = [np.dot(n, l) * (k_d[0] * light.diffuse[0]),
	                	  np.dot(n, l) * (k_d[1] * light.diffuse[1]),
	                	  np.dot(n, l) * (k_d[2] * light.diffuse[2])]

	                Is = [(k_s[0] * light.specular[0]) * np.dot(v, r),
	                	  (k_s[1] * light.specular[1]) * np.dot(v, r),
	                	  (k_s[2] * light.specular[2]) * np.dot(v, r)]

	                color = color + Id + Is

			pixel = color

        return points_window
