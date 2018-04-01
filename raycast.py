import numpy as np
from elements import *


def apply_mwc(matrix_wc, scene):
    for obj in scene.objects:
        obj.apply_transformation(matrix_wc)
    return scene


def apply_mcw(matrix_cw, scene):
    for obj in scene.objects:
        obj.apply_transformation(matrix_cw)
    return scene


def render(window, scene, camera, n, m):
    rgb_array = np.zeros((n, m, 3))

    for i in range(n):
        for j in range(m):
            rgb_array[i, j] = scene.background_color 

            x = window[i, j][0]
            y = window[i, j][1]
            z = window[i, j][2]
            pixel = Point('p', x, y, z)

            ray = pixel.to_vector()
            ray = ray.normalize()

            t = 999999
            for obj in scene.objects:
                if obj.intercepts_aura(ray):
                    #print ("achei uma intersecao com aura")
                    visible_faces = obj.backface_culling(ray)

                    for face in visible_faces:
                        Pin = face.get_Pin(ray)

                        if face.contains(Pin):
                            #print ("achei uma intercao com objeto")
                            n = face.get_normal()
                            v = face.points[0]
                            new_t = np.dot(v.coordinates, n.coordinates) / np.dot(pixel.coordinates, n.coordinates)
                            if new_t < t:
                                #print ("calculando rgb do ponto")

                                #CALCULANDO RGB DO PONTO Pin
                                v = Vector(Pin, camera)
                                f = Pin.get_face()
                                n = f.get_normal()

                                Ka = Pin.material.k_a
                                Ia = [Ka[0] * scene.ambient_light[0],
                                    Ka[1] * scene.ambient_light[1],
                                    Ka[2] * scene.ambient_light[2]]
                                color = np.array(Ia)

                                for light in scene.lights:
                                    light_source = Point('', light.position[0], light.position[1], light.position[2])

                                    l = Vector(Pin, light_source)
                                    l_normal = l.normalize()
                                    r = ((2 * np.dot(n, l_normal)) * n) - l_normal
                                    r_normal = r.normalize()
                                    # procurar intersecao entre l e algum obj do cenario
                                    intersection = False
                                    for obj in scene.objects:
                                        if obj.intercepts(l):
                                            intersection = True
                                            break

                                    if not intersection:
                                        # calcula Id, Is e soma a color
                                        diffuse_attenuation = np.dot(n.coordinates, l.coordinates)
                                        Kd = window[i, j].material.k_d
                                        Id = [diffuse_attenuation * Kd[0] * light.diffuse[0],
                                            diffuse_attenuation * Kd[1] * light.diffuse[1],
                                            diffuse_attenuation * Kd[2] * light.diffuse[2]]

                                        color = color + np.array(Id)

                                        m = Pin.material.m
                                        specular_attenuation = np.dot(v.coordinates, r.coordinates) ** m
                                        Is = [Ks[0] * light.specular[0] * specular_attenuation,
                                            Ks[1] * light.specular[1] * specular_attenuation,
                                            Ks[2] * light.specular[2] * specular_attenuation]
                                        
                                        color = color + np.array(Is)
                                rgb_array[i, j] = color

    return rgb_array



class Window():
    def __init__(self, params):
        self.d = params[0]
        self.n = params[1]
        self.m = params[2]
        self.W = params[3]
        self.H = params[4]

        self.deltaX = self.W / self.m
        self.deltaY = self.H / self.n

        self.window = np.zeros((self.n, self.m, 3))

        for i in range(self.n):
            for j in range(self.m):
                x = -(self.W / 2) + (self.deltaX / 2) + j * self.deltaX
                y = (self.H / 2) - (self.deltaY / 2) - i * self.deltaY

                self.window[i, j] = [x, y, -self.d]

    def get_window(self):
        return self.window
