import numpy as numpy
import object
import camera
import scene
import transformations

###		SCENE PARAMETERS	###
#scene_model = 			#file containing scene description
light_coordinates = []
camera_coordinates = []
look_at = []

###		WINDOW PARAMETERS	 ###
d = 
W = 
H = 
n = 
m = 
window_params = [d, n, m, W, H]

###		RAYCASTING		###
#define raycast steps and functions here
def raycast_intersection(window, scene):
	new_window = np.matlib.zeros(n, m)

	for pixel in window.flat:
		pixel = pixel.to_vector()

		for obj in scene.objects:
			#verificar se existe intersecao entre raio e aura do obj, funcao booleana
			'''
			if pixel.aura_interception(obj):
				visible_faces = obj.backface_culling(pixel)

				for face in visible_faces:
					#caculate interception, then check if t is smaller than the one currently in auxiliary variable (checks if point is in front of the others)
					#make dictinary of intersection points, t is used as key
					#barycentric coordinates go in here or before the test stated above?

					#place point in new_window
			'''

	return new_window

#define raycast function to calculate colors using matrix returned from the function above
def raycast_color(points_window, scene):
	color_window = np.matlib.zeros(n, m)

	return color_window


##	BUILDING SCENE AND SETTING CAMERA 	##
scene = Scene.__init__(light_coordinates)
scene.build_obj(scene_model)

camera = Camera.__init__(camera_coordinates, look_at)

wc_matrix = camera.world_to_camera_matrix()
scene.apply_mwc(wc_matrix)

visualization_window = camera.build_window(window_params)
points_window = raycast_intersection(visualization_window, scene)
colors_window = raycast_color(points_window, scene)








