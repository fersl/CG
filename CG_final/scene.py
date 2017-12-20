import numpy as np
from Shapes import *
from transformations import *
from raycast import Punctual_Light, Spot_light


class Scene(object):
    def __init__(self):
        self.objects = {}
        self.lights = {}
        self.materials = {}
        self.ambient_light = [0.1, 0.1, 0.1]

    def add_light(self, light):
        light_id = len(self.lights) + 1
        self.lights[light_id] = light
