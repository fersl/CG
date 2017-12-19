import numpy as np
from Objects import *
from object import *
from transformations import *
from raycast import Punctual_Light, Spot_light

class Scene(object):
	def __init__(self):
		self.objects = {}
		self.lights = {}
		self.ambient_light = [0.1, 0.1, 0.1]

	def add_light(self, light):
		light_id = len(self.lights) + 1
		self.lights[light_id] = light

	

"""
	def ???(self, file):
		#recebe um arquivo com a descrição da cena e vai criando e adicionando objetos aqui, já com coordenadas finais e material das faces definido
		#no arquivo declaramos os objetos básicos e aplicamos as devidas transformações para posicioná-los como queremos
		#fucking materiais. sempre eles.

		#como estruturar o arquivo de descrição da cena para então escrever essa função....

		with open (file) as file:
			for line in file:
				line.strip()
				data = line.split()

				if data[0] == '': continue

				elif data[0] == '#': continue

				elif data[0] == 'o':
					obj = Object.__init__(data[1])
					obj.build(data[2])
					self.objects[data[1]] = obj

					#descrição das transformações aplicadas ao objeto?
					#descrição das cores

"""

	