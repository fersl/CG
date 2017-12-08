import numpy as np

#def apply_transformation(object, matrix):

###		ESCALA		###

def scale_matrix(s):
	return np.array([
					[s[0], 0, 0, 0],
					[0, s[1], 0, 0],
					[0, 0, s[2], 0],
					[0, 0, 0, 1]])


###		TRANSLAÇÃO		###

def translation_matrix(t):
	return np.array([
					[1, 0, 0, t[0]],
					[0, 1, 0, t[1]],
					[0, 0, 1, t[2]],
					[0, 0, 0, 1]])


###		CISALHAMENTO	###

def shearXY_matrix(angle):
	tg = np.tan(rad(angle))
	return np.array([
					[1, 0, 0, 0]
					[tg, 1, 0, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])

def shearXZ_matrix(angle):
	tan = np.tan(rad(angle))
	return np.array([
					[1, 0, 0, 0]
					[0, 1, 0, 0]
					[tg, 0, 1, 0]
					[0, 0, 0, 1]])

def shearYX_matrix(angle):
	tan = np.tan(rad(angle))
	return np.array([
					[1, tg, 0, 0]
					[0, 1, 0, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])

def shearYZ_matrix(angle):
	tan = np.tan(rad(angle))
	return np.array([
					[1, 0, 0, 0]
					[0, 1, 0, 0]
					[0, tg, 1, 0]
					[0, 0, 0, 1]])

def shearZX_matrix(angle):
	tan = np.tan(rad(angle))
	return np.array([
					[1, 0, tg, 0]
					[0, 1, 0, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])

def shearZY_matrix(angle):
	tan = np.tan(rad(angle))
	return np.array([
					[1, 0, 0, 0]
					[0, 1, tg, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])


###		REFLEXÃO	###

def reflectionXY_matrix():
	return np.array([
					[1, 0, 0, 0]
					[0, 1, 0, 0]
					[0, 0, -1, 0]
					[0, 0, 0, 1]])

def reflectionXZ_matrix():
	return np.array([
					[1, 0, 0, 0]
					[0, -1, 0, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])

def reflectionYZ_matrix():
	return np.array([
					[-1, 0, 0, 0]
					[0, 1, 0, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])

#def arbitrary_reflection_matrix():


###		ROTAÇÃO		###

def rotationX_matrix(angle):
	sin = np.sin(np.radians(angle))
	cos = np.cos(np.radians(angle))

	return np.array([
					[1, 0, 0, 0]
					[0, cos, -sin, 0]
					[0, sin, cos, 0]
					[0, 0, 0, 1]])

def rotationY_matrix(angle):
	sin = np.sin(np.radians(angle))
	cos = np.cos(np.radians(angle))

	return np.array([
					[cos, 0, sin, 0]
					[0, 1, 0, 0]
					[-sin, 0, cos, 0]
					[0, 0, 0, 1]])

def rotationZ_matrix(angle):
	sin = np.sin(np.radians(angle))
	cos = np.cos(np.radians(angle))

	return np.array([
					[cos, -sin, 0, 0]
					[sin, cos, 0, 0]
					[0, 0, 1, 0]
					[0, 0, 0, 1]])

#def arbitrary_rotation_matrix(angle):