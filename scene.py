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

'''
	def add_obj(self, file):
		obj_id = len(self.objects)+1
		obj = obj.Object.__init__(obj_id)
		obj.build()
		self.objects.append(obj)
'''

	def apply_mwc(self, mwc):
		for obj in scene.objects:
			obj.apply_transformation(mwc)