###		RAYCASTING		###
def raycast_intersection(window, scene):
	new_window = np.matlib.zeros(n, m)

	for pixel in window.flat:
		ray = pixel.to_vector()
		#ray = ray.normalize()
		Pin = [999999, None]

		for obj in scene.objects:
			if obj.aura_interception(pixel):
				visible_faces = obj.backface_culling(pixel)

				for face in visible_faces:
					aux = face.find_Pin(ray)

					if face.contains(aux):
						if aux[0] < Pin[0]:
							Pin = aux
		pixel = Pin[1]

	return new_window

#define raycast function to calculate colors using matrix returned from the function above
def raycast_color(points_window, scene):
	color_window = np.matlib.zeros(n, m)

	return color_window