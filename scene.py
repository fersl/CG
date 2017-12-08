import numpy as numpy
import object as obj
import transformations

class scene(object):
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