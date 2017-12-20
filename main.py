
###		TO DO 	  ###
# montar cena

# calcular cores e iluminação e sombra
# montar funções para exibição da cena na tela

# adicionar perspectiva à janela de visualização

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mp3d
from basic_elements import *
from raycast import *
import scene

"""
###		SCENE PARAMETERS	###
#scene_model = 			#file containing scene description
light_coordinates = []
camera_coordinates = []
look_at = []
avup = []
"""

"""
###		WINDOW PARAMETERS	 ###
d = 
W = 
H = 
n = 
m = 
window_params = [d, n, m, W, H]
"""



##	BUILDING SCENE AND SETTING CAMERA 	##
# scene = Scene.__init__()		#this should build scene and return a list of objects

camera = Camera.__init__(camera_coordinates, look_at, avup)

wc_matrix = camera.world_to_camera_matrix()
Raycast.apply_mwc(wc_matrix, scene)

visualization_window = Raycast.build_window(window_params)
points_window = Raycast.intersection_window(visualization_window, scene)
colors_window = Raycast.color_window(points_window, scene)

# use colors_window here to print scene to screen
