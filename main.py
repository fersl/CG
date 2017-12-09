
	#aplicar raycast em cada um dos pontos da janela
		#definir equação da reta que passa pelo ponto
		#calcular interseção entre raio e aura de cada objeto 
			#se ouver interseção, aplicar função de backface culling no objeto (função retorna uma lista de faces)
			#calcular interseção do raio com o plano de cada face (devemos ter uma lista de pontos de interseção aqui)
				#aqui em cima isso será calculado por outra função
			#calcular coordenadas baricentricas para ver se o ponto reamente pertence a face
				#se realmente pertencer a face, append

import numpy as numpy
import object
import camera
import scene
import transformations

scene_model = 
light = []
camera_coordinates = []
look_at = []

###		WINDOW PARAMETERS	 ###
d = 
W = 
H = 
n = 
m = 
window_params = [d, n, m, W, H]

##	BUILDING SCENE AND SETTING CAMERA 	##
scene = Scene.__init__(light)
scene.build_obj(scene_model)
camera = Camera.__init__(camera_coordinates, look_at)

def apply_mwc(scene, camera):
	mwc = camera.world_to_camera_matrix()
	for obj in scene.objects:
		obj.apply_transformation(mwc)
	return scene.objects

window = camera.build_window(window_params)
#usar essa janela pra aplicar raycast







