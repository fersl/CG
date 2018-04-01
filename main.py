import numpy as np
import matplotlib.pyplot as plt
from raycast import *
from scene import *
from elements import *
import random

###		CAMERA		###
camera_coordinates = [-5.0, 15.0, -20.0]
camera = Point('camera', camera_coordinates[0], camera_coordinates[1], camera_coordinates[2])
look_at = [5.0, 5.0, -5.0]
avup = [5.0, 6.0, -5.0]


###		WINDOW		###
d = 0.5
W = 1
H = 1
n = 100
m = 100
window_params = [d, n, m, W, H]

###		RGB TEST	###

rgb_array_test = np.zeros((n, m, 3))
for i in range(n):
	for j in range(m):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		rgb_array_test[i, j] = [r/255, g/255, b/255]


###		BUILDING SCENE		###

scene = Scene()
camera_obj = Camera(camera_coordinates, look_at, avup)
mwc = camera_obj.world_to_camera_matrix()
scene = apply_mcw(mwc, scene)

###		BUILDING WINDOW		###
window = Window(window_params).get_window()
rgb_array = render(window, scene, camera, n, m)

plt.subplot(211)
plt.imshow(rgb_array_test)
plt.subplot(212)
plt.imshow(rgb_array)
plt.show()
