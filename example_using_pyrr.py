import math

from pyrr import Quaternion, Matrix44, Vector3

import numpy as np

print("#########################################")

#np.set_printoptions(precision=3)
np.set_printoptions(formatter={'float': '{: 8.3f}'.format})
#np.set_printoptions(suppress=True)

location_v = Vector3([5.0, 6.0, 7.0])
location_m = Matrix44.from_translation(location_v)

print("Location Matrix")

print("")

#print(location_m)
transform_flat = location_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

print("#########################################")

deg = -10
rad = (deg * np.pi / 180)
q_rot = Quaternion.from_x_rotation(rad)

q_array = np.array(q_rot, np.float32)

rotation_m = Matrix44(q_rot)

print("Rotation Matrix - X")

print("")

print(q_array)

#print(rotation_m)
transform_flat = rotation_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

print("#########################################")

deg = -10
rad = (deg * np.pi / 180)
q_rot = Quaternion.from_y_rotation(rad)

q_array = np.array(q_rot, np.float32)

rotation_m = Matrix44(q_rot)

print("Rotation Matrix - Y")

print("")

print(q_array)

#print(rotation_m)
transform_flat = rotation_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

print("#########################################")

deg = -10
rad = (deg * np.pi / 180)
q_rot = Quaternion.from_z_rotation(rad)

q_array = np.array(q_rot, np.float32)

rotation_m = Matrix44(q_rot)

print("Rotation Matrix - Z")

print("")

print(q_array)

#print(rotation_m)
transform_flat = rotation_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

print("#########################################")

displacement_v = Vector3([10.0, 0.0, 0])
displacement_m = Matrix44.from_translation(displacement_v)

print("Translate Matrix")

print("")

#print(displacement_m)
transform_flat = displacement_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

print("#########################################")

print("Translate and Rotate")

print("")

print("")

mvMatrix_tmp = displacement_m*location_m
transform_flat = mvMatrix_tmp.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

mvMatrix = rotation_m*mvMatrix_tmp
transform_flat = mvMatrix.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

print("#########################################")

print("Rotate and Translate")

print("")

transform_flat = rotation_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

transform_flat = location_m.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

mvMatrix_tmp = rotation_m*location_m
transform_flat = mvMatrix_tmp.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

mvMatrix = displacement_m*mvMatrix_tmp
transform_flat = mvMatrix.flatten()	
transform_array = np.array(transform_flat, np.float32)
print(transform_array)

print("")

