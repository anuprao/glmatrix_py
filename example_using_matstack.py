#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

from glmatrix import *

import numpy as np

print("#########################################")

#np.set_printoptions(precision=3)
np.set_printoptions(formatter={'float': '{: 8.3f}'.format})
#np.set_printoptions(suppress=True)

location_v = vec3_create([5.0, 6.0, 7.0])
location_m = gl_mat4_from_translation(location_v)

print("Location Matrix")

print("")

#print(location_m)
transform_array = np.array(location_m, np.float32)
print(transform_array)

print("")

print("#########################################")

deg = -10
rad = (deg * math.pi / 180)
q_rot = gl_quat_from_x_rotation(rad)
rotation_m = mat4_create(None)
gl_mat4_from_quat(q_rot, rotation_m)

print("Rotation Matrix - X")

print("")
transform_array = np.array(q_rot, np.float32)
print(transform_array)

transform_array = np.array(rotation_m, np.float32)
print(transform_array)

print("")

print("#########################################")

deg = -10
rad = (deg * math.pi / 180)
q_rot = gl_quat_from_y_rotation(rad)
rotation_m = mat4_create(None)
gl_mat4_from_quat(q_rot, rotation_m)

print("Rotation Matrix - Y")

print("")
transform_array = np.array(q_rot, np.float32)
print(transform_array)

transform_array = np.array(rotation_m, np.float32)
print(transform_array)

print("")

print("#########################################")

deg = -10
rad = (deg * math.pi / 180)
q_rot = gl_quat_from_z_rotation(rad)
rotation_m = mat4_create(None)
gl_mat4_from_quat(q_rot, rotation_m)

print("Rotation Matrix - Z")

print("")
transform_array = np.array(q_rot, np.float32)
print(transform_array)

transform_array = np.array(rotation_m, np.float32)
print(transform_array)

print("")

print("#########################################")

displacement_v = vec3_create([10.0, 0.0, 0])
displacement_m = gl_mat4_from_translation(displacement_v)

print("Translate Matrix")

print("")

#print(displacement_m)
transform_array = np.array(displacement_m, np.float32)
print(transform_array)

print("")

print("#########################################")

print("Translate and Rotate")

ms = matstack()

print("")

print("")

ms.loadMatrix(location_m)

mvMatrix_tmp = mat4_create(None) 
ms.multMatrix(displacement_m)
ms.getMatrix(mvMatrix_tmp)
transform_array = np.array(mvMatrix_tmp, np.float32)
print(transform_array)

print("")

mvMatrix = mat4_create(None) 
ms.multMatrix(rotation_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("")

print("#########################################")

print("Rotate and Translate")

ms = matstack()

print("")

transform_array = np.array(rotation_m, np.float32)
print(transform_array)

print("")

transform_array = np.array(location_m, np.float32)
print(transform_array)

print("")

ms.loadMatrix(location_m)

mvMatrix_tmp = mat4_create(None) 
ms.multMatrix(rotation_m)
ms.getMatrix(mvMatrix_tmp)
transform_array = np.array(mvMatrix_tmp, np.float32)
print(transform_array)

print("")

mvMatrix = mat4_create(None)  
ms.multMatrix(displacement_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("")

print("#########################################")

print("#########################################")

print("Push / Pop version")

print("")

ms = matstack()

print("Initialise")

ms.loadMatrix(location_m)
mvMatrix = mat4_create(None) 
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Push")

mvMatrix = mat4_create(None)  
ms.pushMatrix()
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Translate")

mvMatrix = mat4_create(None)  
ms.multMatrix(displacement_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Pop")

mvMatrix = mat4_create(None)  
ms.popMatrix()
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("#########################################")

print("Push")

mvMatrix = mat4_create(None)  
ms.pushMatrix()
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Translate")

mvMatrix = mat4_create(None)  
ms.multMatrix(displacement_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Rotate")

mvMatrix = mat4_create(None)  
ms.multMatrix(rotation_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Pop")

mvMatrix = mat4_create(None)  
ms.popMatrix()
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("#########################################")

print("Push")

mvMatrix = mat4_create(None)  
ms.pushMatrix()
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Rotate")

mvMatrix = mat4_create(None)  
ms.multMatrix(rotation_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Translate")

mvMatrix = mat4_create(None)  
ms.multMatrix(displacement_m)
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)

print("Pop")

mvMatrix = mat4_create(None)  
ms.popMatrix()
ms.getMatrix(mvMatrix)
transform_array = np.array(mvMatrix, np.float32)
print(transform_array)
