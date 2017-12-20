import numpy as np
from cube import *
from basic_elements import *
from transformations import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mp3d
#from mpl_toolkits.mplot3d import Axes3D

cube = Cube('teste')

def visualizar(ax, vertices, faces):

    vetorFace = []
    for i in range(len(faces)):
        vetorFace.append(mp3d.art3d.Poly3DCollection([faces[i].getPontos()]))

    for i in range(len(faces)):
        ax.add_collection3d(vetorFace[i])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
visualizar(ax, cube.get_vertices(), cube.get_faces())

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()
