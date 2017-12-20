
###		TO DO 	  ###
# montar cena

# calcular cores e iluminação e sombra
# montar funções para exibição da cena na tela

# adicionar perspectiva à janela de visualização

import numpy as np
import matplotlib.pyplot as plt
from basic_elements import *
from raycast import *
from scene import *


###		SCENE PARAMETERS	###
#scene_model = 			#file containing scene description
#light_coordinates = []
camera_coordinates = [0.0, 0.0, 0.0]
look_at = []
avup = []



###		WINDOW PARAMETERS	 ###
d = 400
W = 600
H = 600
n = 600
m = 600
window_params = [d, n, m, W, H]



##	BUILDING SCENE AND SETTING CAMERA 	##
# scene = Scene()		#this should build scene and return a list of objects
# scene_objs = scene.objects.values()

camera = Camera.__init__(camera_coordinates, look_at, avup)

wc_matrix = camera.world_to_camera_matrix()
Raycast.apply_mwc(wc_matrix, scene_objs)

visualization_window = Raycast.build_window(window_params)
points_window = Raycast.intersection_window(visualization_window, scene_objs)
colors_window = Raycast.color_window(points_window, scene)

plt.imshow(colors_window)
plt.show()
