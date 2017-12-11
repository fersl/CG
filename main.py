#chamar esse arquivo de raycast, criar outro arquivo com as funções para exibir cena na tela, e criar outro arquivo main para unir tudo  e chamar essas funções na ordem certa? ou só criar outro arquivo com as funções de exibição e chamar as funções aqui? ou só juntar tudo aqui?
#segunda opção??

###		TO DO 	  ###
#arrumar e organizar imports

#função para calcular coordenadas baricentricas
#função para ler arquivo e construir objeto

#calcular cores e iluminação e sombra
#montar funções para exibição da cena na tela

#adicionar perspectiva à janela de visualização

import numpy as numpy
import object
import camera
import scene
import transformations
import window

###		SCENE PARAMETERS	###
#scene_model = 			#file containing scene description
light_coordinates = []
camera_coordinates = []
look_at = []
avup = []

###		WINDOW PARAMETERS	 ###
d = 
W = 
H = 
n = 
m = 
window_params = [d, n, m, W, H]



##	BUILDING SCENE AND SETTING CAMERA 	##
scene = Scene.__init__(light_coordinates)
scene.build_obj(scene_model)

camera = Camera.__init__(camera_coordinates, look_at)

wc_matrix = camera.world_to_camera_matrix()
scene.apply_mwc(wc_matrix)

visualization_window = camera.build_window(window_params)
points_window = raycast_intersection(visualization_window, scene)
colors_window = raycast_color(points_window, scene)








