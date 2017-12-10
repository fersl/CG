import numpy as numpy
from Objects.object import *
import transformations
from camera import Camera

class Scene(object):
	def __init__(self, light_coords):
		self.objects = []
		self.light = obj.Point.__init__("light", light_coords)
		self.ambient_light = []
		self.diffuse_light = []

	def build_obj(self, file):
		obj_id = len(self.objects)+1
		obj = obj.Object.__init__(obj_id)
		#ler arquivo e adicionar vertices e faces aqui
		self.objects.append(obj)

	def apply_mwc(self, mwc):
		for obj in scene.objects:
			obj.apply_transformation(mwc)

'''
	def set_camera(self, coordinates, look_at, window_parameters):
		self.camera = Camera.__init__(coordinates, look_at)
		self.camera.calculate_axis()
		matrix = self.camera.world_to_camera_matrix()

		for obj in self.objects:
			obj.apply_transformation(matrix)

		self.window = self.camera.build_window(window_parameters)
'''