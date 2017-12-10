import numpy as np
from Objects.object import Point, Vector

class Camera(object):
	def __init__(position, look_at, avup):
		self.position = Point.__init__("camera", position)
		self.look_at = Point.__init__("look_at", look_at)
		self.avup = Point.__init__("avup", avup)
		self.i
		self.j
		self.k

	def calculate_axis():
		z = Vector.__init__(look_at, position)
		self.k = z.normalize()
		vup = Vector.__init__(position, avup)
		vup = vup.normalize()
		x = np.cross(vup, self.k)
		self.i = x.normalize
		y = n.cross(self.k, self.i)
		self.j = y.normalize
		return [self.i, self.j, self.k]

	def world_to_camera_matrix():
		return np.array([
							[self.i[0], self.i[1], self.i[2], -np.dot(self.i, self.position)],
							[self.j[0], self.j[1], self.j[2], -np.dot(self.j, self.position)],
							[self.k[0], self.k[1], self.k[2], -np.dot(self.k, self.position)],
							[0, 0, 0, 1]])

	def camera_to_world_matrix():
		return np.array([
						[self.i[0], self.j[0], self.k[0], self.position[0]],
						[self.i[1], self.j[1], self.k[1], self.position[1]],
						[self.i[2], self.j[2], self.k[2], self.position[2]],
						[0, 0, 0, 1]])

	def build_window(params):
		points_window = np.matlib.zeros(n, m)

		d = params[0]
		n = params[1]
		m = params[2]
		W = params[3]
		H = params[4]

		deltaX = W / m 
		deltaY = H / n

		for i in range(n):
			x =  -(W / 2)+(deltaX/2) + j*deltaX

			for j in range(m):
				y = (H/2) - (deltaY/2) - i*deltaY

				points_window[i, j] = [x, y, -d]

		return points_window
