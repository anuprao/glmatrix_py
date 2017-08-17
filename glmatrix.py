#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# glmatrixpy
# source code repo at https://github.com/anuprao/glmatrixpy
#
# Ported to Python by Anup Jayapal Rao, https://github.com/anuprao
#
# Code derived from following projects:
# 	gl-matrix.js : https://github.com/toji/gl-matrix by Brandon Jones, https://github.com/toji
#	gl-matrix.c : https://github.com/coreh/gl-matrix.c.git by Marco Aurélio, https://github.com/coreh
#
#
#					|  m0  m4  m8 m12  |   | a b c d |
#   				|  m1  m5  m9 m13  | = | e f g h |
#   				|  m2  m6 m10 m14  |   | i j k l |
#   				|  m3  m7 m11 m15  |   | 0 0 0 1 |
#
#	Translation	T = < d, h, l > = < m12, m13, m14 >
#
#   Scale		S = < Sx, Sy, Sz > 
#		where
#				Sx =    || < a, e, i > ||    =    || <  m0,  m1,  m2 > ||
#				Sy =    || < b, f, j > ||    =    || <  m4,  m5,  m6 > ||
#				Sz =    || < c, g, k > ||    =    || <  m8,  m9, m10 > ||
#
#   Rotation		 
#				| a/Sx  b/Sy  c/Sz     0 |   |   m0/Sx   m4/Sy   m8/Sz       0  |   
#   			| e/Sx  f/Sy  g/Sz     0 | = |   m1/Sx   m5/Sy   m9/Sz       0  |
#   			| i/Sx  j/Sy  k/Sz     0 |   |   m2/Sx   m6/Sy  m10/Sz       0  |   
#   			|    0     0     0     1 |   |       0       0       0       1  |   
#

################################################################################

import sys
from math import *

################################################################################

def vec3_create(vec):

	dest = [0.0]*3

	if (vec):
		dest[0] = vec[0]
		dest[1] = vec[1]
		dest[2] = vec[2]
	
	else:
		dest[0] = dest[1] = dest[2] = 0

	return dest

def vec3_set(vec, dest):

	dest[0] = vec[0]
	dest[1] = vec[1]
	dest[2] = vec[2]

	return dest

def vec3_add(vec, vec2, dest):

	if (None==dest or vec == dest):
		vec[0] = vec[0] + vec2[0]
		vec[1] = vec[1] + vec2[1]
		vec[2] = vec[2] + vec2[2]
		
		return vec
	
	dest[0] = vec[0] + vec2[0]
	dest[1] = vec[1] + vec2[1]
	dest[2] = vec[2] + vec2[2]

	return dest

def vec3_subtract(vec, vec2, dest):

	if (None==dest or vec == dest):
		vec[0] = vec[0] - vec2[0]
		vec[1] = vec[1] - vec2[1]
		vec[2] = vec[2] - vec2[2]
		
		return vec

	dest[0] = vec[0] - vec2[0]
	dest[1] = vec[1] - vec2[1]
	dest[2] = vec[2] - vec2[2]
	
	return dest

def vec3_multiply(vec, vec2, dest):

	if (None==dest or vec == dest):
		vec[0] = vec[0] * vec2[0]
		vec[1] = vec[1] * vec2[1]
		vec[2] = vec[2] * vec2[2]
		
		return vec

	dest[0] = vec[0] * vec2[0]
	dest[1] = vec[1] * vec2[1]
	dest[2] = vec[2] * vec2[2]
	
	return dest

def vec3_negate(vec, dest):

	if (None==dest):
		dest = vec
	
	dest[0] = -vec[0]
	dest[1] = -vec[1]
	dest[2] = -vec[2]
	
	return dest

def vec3_scale(vec, val, dest):

	if (None==dest or vec == dest):
		
		vec[0] = vec[0] * val
		vec[1] = vec[1] * val
		vec[2] = vec[2] * val
		
		return vec

	dest[0] = vec[0] * val
	dest[1] = vec[1] * val
	dest[2] = vec[2] * val
	
	return dest

def vec3_normalize(vec, dest):

	if (None==dest):
		dest = vec

	x = vec[0]
	y = vec[1]
	z = vec[2]
	
	len = sqrt(x * x + y * y + z * z)

	if (None==len):
		
		dest[0] = 0
		dest[1] = 0
		dest[2] = 0
		
		return dest
	
	elif (len == 1.0):
		
		dest[0] = x
		dest[1] = y
		dest[2] = z
		
		return dest

	len = 1 / len
	dest[0] = x * len
	dest[1] = y * len
	dest[2] = z * len
	
	return dest

def vec3_cross(vec, vec2, dest):

	if (None==dest):
		dest = vec
	
	x = vec[0]
	y = vec[1]
	z = vec[2]
	x2 = vec2[0]
	y2 = vec2[1]
	z2 = vec2[2]

	dest[0] = y * z2 - z * y2
	dest[1] = z * x2 - x * z2
	dest[2] = x * y2 - y * x2
	
	return dest

def vec3_length(vec):

	x = vec[0] 
	y = vec[1]
	z = vec[2]
	
	return sqrt(x * x + y * y + z * z)

def vec3_dot(vec, vec2):

	return vec[0] * vec2[0] + vec[1] * vec2[1] + vec[2] * vec2[2]

def vec3_direction(vec, vec2, dest):

	if (None==dest):
		dest = vec
	
	x = vec[0] - vec2[0]
	y = vec[1] - vec2[1]
	z = vec[2] - vec2[2]
	len = sqrt(x * x + y * y + z * z)

	if (None==len):
		dest[0] = 0
		dest[1] = 0
		dest[2] = 0
		
		return dest

	len = 1 / len
	dest[0] = x * len
	dest[1] = y * len
	dest[2] = z * len
	
	return dest

def vec3_lerp(vec, vec2, lerp, dest):

	if (None==dest):
		dest = vec

	dest[0] = vec[0] + lerp * (vec2[0] - vec[0])
	dest[1] = vec[1] + lerp * (vec2[1] - vec[1])
	dest[2] = vec[2] + lerp * (vec2[2] - vec[2])

	return dest

def vec3_dist(vec, vec2):

	x = vec2[0] - vec[0]
	y = vec2[1] - vec[1]
	z = vec2[2] - vec[2]

	return sqrt(x * x + y * y + z * z)

def vec3_unproject(vec, view, proj, viewport, dest):

	if (None==dest):
		dest = vec

	m = mat4_create(None)
	v = [0]*4

	v[0] = (vec[0] - viewport[0]) * 2.0 / viewport[2] - 1.0
	v[1] = (vec[1] - viewport[1]) * 2.0 / viewport[3] - 1.0
	v[2] = 2.0 * vec[2] - 1.0
	v[3] = 1.0

	mat4_multiply(proj, view, m)
	
	if (None==mat4_inverse(m, None)):
		return None
	
	mat4_multiplyVec4(m, v, None)
	
	if (v[3] == 0.0):
		return None
	
	dest[0] = v[0] / v[3]
	dest[1] = v[1] / v[3]
	dest[2] = v[2] / v[3]

	return dest

################################################################################

def vec4_create(vec):

	dest = [0.0]*4

	if (vec):
		dest[0] = vec[0]
		dest[1] = vec[1]
		dest[2] = vec[2]
		dest[3] = vec[3]
	
	else:
		dest[0] = dest[1] = dest[2] = dest[3] = 0

	return dest
	
def vec4_set(vec, dest):

	dest[0] = vec[0]
	dest[1] = vec[1]
	dest[2] = vec[2]
	dest[3] = vec[3]
	
	return dest
	
################################################################################

def mat3_create(mat):
	dest = [0.0]*9
	
	if None != mat :
		dest[0] = mat[0]
		dest[1] = mat[1]
		dest[2] = mat[2]
		dest[3] = mat[3]
		dest[4] = mat[4]
		dest[5] = mat[5]
		dest[6] = mat[6]
		dest[7] = mat[7]
		dest[8] = mat[8]
	
	return dest

def mat3_set(mat, dest):
	dest[0] = mat[0]
	dest[1] = mat[1]
	dest[2] = mat[2]
	dest[3] = mat[3]
	dest[4] = mat[4]
	dest[5] = mat[5]
	dest[6] = mat[6]
	dest[7] = mat[7]
	dest[8] = mat[8]
	
	return dest

def mat3_identity(dest):

	if None == dest :
		dest = mat3_create(None)
	
	dest[0] = 1
	dest[1] = 0
	dest[2] = 0
	
	dest[3] = 0
	dest[4] = 1
	dest[5] = 0
	
	dest[6] = 0
	dest[7] = 0
	dest[8] = 1
	
	return dest

def mat3_transpose(mat, dest):

	# If we are transposing ourselves we can skip a few steps but have to cache some values
	if (None == dest) or (mat == dest):
	
		a01 = mat[1]
		a02 = mat[2]
		a12 = mat[5]

		mat[1] = mat[3]
		mat[2] = mat[6]
		mat[3] = a01
		mat[5] = mat[7]
		mat[6] = a02
		mat[7] = a12
		
		return mat
	
	dest[0] = mat[0]
	dest[1] = mat[3]
	dest[2] = mat[6]
	dest[3] = mat[1]
	dest[4] = mat[4]
	dest[5] = mat[7]
	dest[6] = mat[2]
	dest[7] = mat[5]
	dest[8] = mat[8]
	
	return dest

def mat3_toMat4(mat, dest):

	if None == dest:
		dest = mat4_create(None)
	
	dest[15] = 1
	dest[14] = 0
	dest[13] = 0
	dest[12] = 0

	dest[11] = 0
	dest[10] = mat[8]
	dest[9] = mat[7]
	dest[8] = mat[6]

	dest[7] = 0
	dest[6] = mat[5]
	dest[5] = mat[4]
	dest[4] = mat[3]

	dest[3] = 0
	dest[2] = mat[2]
	dest[1] = mat[1]
	dest[0] = mat[0]

	return dest

################################################################################

def mat4_create(mat):

	dest = [0.0]*16

	if (mat):
		dest[0] = mat[0]
		dest[1] = mat[1]
		dest[2] = mat[2]
		dest[3] = mat[3]
		dest[4] = mat[4]
		dest[5] = mat[5]
		dest[6] = mat[6]
		dest[7] = mat[7]
		dest[8] = mat[8]
		dest[9] = mat[9]
		dest[10] = mat[10]
		dest[11] = mat[11]
		dest[12] = mat[12]
		dest[13] = mat[13]
		dest[14] = mat[14]
		dest[15] = mat[15]

	return dest

def mat4_set(mat, dest):

	dest[0] = mat[0]
	dest[1] = mat[1]
	dest[2] = mat[2]
	dest[3] = mat[3]
	dest[4] = mat[4]
	dest[5] = mat[5]
	dest[6] = mat[6]
	dest[7] = mat[7]
	dest[8] = mat[8]
	dest[9] = mat[9]
	dest[10] = mat[10]
	dest[11] = mat[11]
	dest[12] = mat[12]
	dest[13] = mat[13]
	dest[14] = mat[14]
	dest[15] = mat[15]
	
	return dest

def mat4_identity(dest):

	if (None==dest):
	
		dest = mat4_create(None)
	
	dest[0] = 1
	dest[1] = 0
	dest[2] = 0
	dest[3] = 0
	
	dest[4] = 0
	dest[5] = 1
	dest[6] = 0
	dest[7] = 0
	
	dest[8] = 0
	dest[9] = 0
	dest[10] = 1
	dest[11] = 0
	
	dest[12] = 0
	dest[13] = 0
	dest[14] = 0
	dest[15] = 1
	
	return dest

def mat4_transpose(mat, dest):

	#If we are transposing ourselves we can skip a few steps but have to cache some values
	if (None==dest or mat == dest):
	
		a01 = mat[1] 
		a02 = mat[2] 
		a03 = mat[3]
		a12 = mat[6] 
		a13 = mat[7] 
		a23 = mat[11]

		mat[1] = mat[4]
		mat[2] = mat[8]
		mat[3] = mat[12]
		mat[4] = a01
		mat[6] = mat[9]
		mat[7] = mat[13]
		mat[8] = a02
		mat[9] = a12
		mat[11] = mat[14]
		mat[12] = a03
		mat[13] = a13
		mat[14] = a23
		
		return mat
	
	dest[0] = mat[0]
	dest[1] = mat[4]
	dest[2] = mat[8]
	dest[3] = mat[12]
	dest[4] = mat[1]
	dest[5] = mat[5]
	dest[6] = mat[9]
	dest[7] = mat[13]
	dest[8] = mat[2]
	dest[9] = mat[6]
	dest[10] = mat[10]
	dest[11] = mat[14]
	dest[12] = mat[3]
	dest[13] = mat[7]
	dest[14] = mat[11]
	dest[15] = mat[15]
	
	return dest

def mat4_determinant(mat):

	#Cache the matrix values (makes for huge speed increases!)
	a00 = mat[0] 
	a01 = mat[1] 
	a02 = mat[2] 
	a03 = mat[3]
	a10 = mat[4] 
	a11 = mat[5] 
	a12 = mat[6] 
	a13 = mat[7]
	a20 = mat[8] 
	a21 = mat[9] 
	a22 = mat[10] 
	a23 = mat[11]
	a30 = mat[12] 
	a31 = mat[13] 
	a32 = mat[14] 
	a33 = mat[15]

	return (a30 * a21 * a12 * a03 - a20 * a31 * a12 * a03 -
			a30 * a11 * a22 * a03 + a10 * a31 * a22 * a03 +
			a20 * a11 * a32 * a03 - a10 * a21 * a32 * a03 -
			a30 * a21 * a02 * a13 + a20 * a31 * a02 * a13 +
			a30 * a01 * a22 * a13 - a00 * a31 * a22 * a13 -
			a20 * a01 * a32 * a13 + a00 * a21 * a32 * a13 +
			a30 * a11 * a02 * a23 - a10 * a31 * a02 * a23 -
			a30 * a01 * a12 * a23 + a00 * a31 * a12 * a23 +
			a10 * a01 * a32 * a23 - a00 * a11 * a32 * a23 -
			a20 * a11 * a02 * a33 + a10 * a21 * a02 * a33 +
			a20 * a01 * a12 * a33 - a00 * a21 * a12 * a33 -
			a10 * a01 * a22 * a33 + a00 * a11 * a22 * a33)

def mat4_inverse(mat, dest):

	if (None==dest):
	
		dest = mat
	
	#Cache the matrix values (makes for huge speed increases!)
	a00 = mat[0] 
	a01 = mat[1] 
	a02 = mat[2] 
	a03 = mat[3]
	a10 = mat[4] 
	a11 = mat[5] 
	a12 = mat[6] 
	a13 = mat[7]
	a20 = mat[8] 
	a21 = mat[9] 
	a22 = mat[10] 
	a23 = mat[11]
	a30 = mat[12] 
	a31 = mat[13] 
	a32 = mat[14] 
	a33 = mat[15]
	b00 = a00 * a11 - a01 * a10
	b01 = a00 * a12 - a02 * a10
	b02 = a00 * a13 - a03 * a10
	b03 = a01 * a12 - a02 * a11
	b04 = a01 * a13 - a03 * a11
	b05 = a02 * a13 - a03 * a12
	b06 = a20 * a31 - a21 * a30
	b07 = a20 * a32 - a22 * a30
	b08 = a20 * a33 - a23 * a30
	b09 = a21 * a32 - a22 * a31
	b10 = a21 * a33 - a23 * a31
	b11 = a22 * a33 - a23 * a32
	d =	(b00 * b11 - b01 * b10 + b02 * b09 + b03 * b08 - b04 * b07 + b05 * b06)

	#Calculate the determinant
	if (None==d):
	
		return None
	
	invDet = 1 / d

	dest[0] = (a11 * b11 - a12 * b10 + a13 * b09) * invDet
	dest[1] = (-a01 * b11 + a02 * b10 - a03 * b09) * invDet
	dest[2] = (a31 * b05 - a32 * b04 + a33 * b03) * invDet
	dest[3] = (-a21 * b05 + a22 * b04 - a23 * b03) * invDet
	dest[4] = (-a10 * b11 + a12 * b08 - a13 * b07) * invDet
	dest[5] = (a00 * b11 - a02 * b08 + a03 * b07) * invDet
	dest[6] = (-a30 * b05 + a32 * b02 - a33 * b01) * invDet
	dest[7] = (a20 * b05 - a22 * b02 + a23 * b01) * invDet
	dest[8] = (a10 * b10 - a11 * b08 + a13 * b06) * invDet
	dest[9] = (-a00 * b10 + a01 * b08 - a03 * b06) * invDet
	dest[10] = (a30 * b04 - a31 * b02 + a33 * b00) * invDet
	dest[11] = (-a20 * b04 + a21 * b02 - a23 * b00) * invDet
	dest[12] = (-a10 * b09 + a11 * b07 - a12 * b06) * invDet
	dest[13] = (a00 * b09 - a01 * b07 + a02 * b06) * invDet
	dest[14] = (-a30 * b03 + a31 * b01 - a32 * b00) * invDet
	dest[15] = (a20 * b03 - a21 * b01 + a22 * b00) * invDet

	return dest

def mat4_toRotationMat(mat, dest):

	if (None==dest):
		dest = mat4_create(None)

	dest[0] = mat[0]
	dest[1] = mat[1]
	dest[2] = mat[2]
	dest[3] = mat[3]
	dest[4] = mat[4]
	dest[5] = mat[5]
	dest[6] = mat[6]
	dest[7] = mat[7]
	dest[8] = mat[8]
	dest[9] = mat[9]
	dest[10] = mat[10]
	dest[11] = mat[11]
	dest[12] = 0
	dest[13] = 0
	dest[14] = 0
	dest[15] = 1

	return dest

def mat4_toMat3(mat, dest):

	if (None==dest):
	
		dest = mat3_create(None)
	

	dest[0] = mat[0]
	dest[1] = mat[1]
	dest[2] = mat[2]
	dest[3] = mat[4]
	dest[4] = mat[5]
	dest[5] = mat[6]
	dest[6] = mat[8]
	dest[7] = mat[9]
	dest[8] = mat[10]

	return dest

def mat4_toInverseMat3(mat, dest):

	#Cache the matrix values (makes for huge speed increases!)
	a00 = mat[0]
	a01 = mat[1]
	a02 = mat[2]
	a10 = mat[4]
	a11 = mat[5]
	a12 = mat[6]
	a20 = mat[8]
	a21 = mat[9]
	a22 = mat[10]
	b01 = a22 * a11 - a12 * a21
	b11 = -a22 * a10 + a12 * a20
	b21 = a21 * a10 - a11 * a20
	d = a00 * b01 + a01 * b11 + a02 * b21

	if (None==d):
		return None
	
	id = 1 / d

	if (None==dest):
		dest = mat3_create(None)
	
	dest[0] = b01 * id
	dest[1] = (-a22 * a01 + a02 * a21) * id
	dest[2] = (a12 * a01 - a02 * a11) * id
	dest[3] = b11 * id
	dest[4] = (a22 * a00 - a02 * a20) * id
	dest[5] = (-a12 * a00 + a02 * a10) * id
	dest[6] = b21 * id
	dest[7] = (-a21 * a00 + a01 * a20) * id
	dest[8] = (a11 * a00 - a01 * a10) * id

	return dest

def mat4_multiply(mat, mat2, dest=None):

	if (None==dest):
		dest = mat
	
	#Cache the matrix values (makes for huge speed increases!)
	a00 = mat[0] 
	a01 = mat[1] 
	a02 = mat[2] 
	a03 = mat[3]
	a10 = mat[4] 
	a11 = mat[5] 
	a12 = mat[6] 
	a13 = mat[7]
	a20 = mat[8] 
	a21 = mat[9] 
	a22 = mat[10] 
	a23 = mat[11]
	a30 = mat[12] 
	a31 = mat[13] 
	a32 = mat[14] 
	a33 = mat[15]
	
	b00 = mat2[0]
	b01 = mat2[1]
	b02 = mat2[2]
	b03 = mat2[3]
	b10 = mat2[4]
	b11 = mat2[5]
	b12 = mat2[6] 
	b13 = mat2[7]
	b20 = mat2[8]
	b21 = mat2[9] 
	b22 = mat2[10] 
	b23 = mat2[11]
	b30 = mat2[12]
	b31 = mat2[13] 
	b32 = mat2[14] 
	b33 = mat2[15]

	dest[0]  = b00 * a00 + b01 * a10 + b02 * a20 + b03 * a30
	dest[1]  = b00 * a01 + b01 * a11 + b02 * a21 + b03 * a31
	dest[2]  = b00 * a02 + b01 * a12 + b02 * a22 + b03 * a32
	dest[3]  = b00 * a03 + b01 * a13 + b02 * a23 + b03 * a33
	
	dest[4]  = b10 * a00 + b11 * a10 + b12 * a20 + b13 * a30
	dest[5]  = b10 * a01 + b11 * a11 + b12 * a21 + b13 * a31
	dest[6]  = b10 * a02 + b11 * a12 + b12 * a22 + b13 * a32
	dest[7]  = b10 * a03 + b11 * a13 + b12 * a23 + b13 * a33
	
	dest[8]  = b20 * a00 + b21 * a10 + b22 * a20 + b23 * a30
	dest[9]  = b20 * a01 + b21 * a11 + b22 * a21 + b23 * a31
	dest[10] = b20 * a02 + b21 * a12 + b22 * a22 + b23 * a32
	dest[11] = b20 * a03 + b21 * a13 + b22 * a23 + b23 * a33
	
	dest[12] = b30 * a00 + b31 * a10 + b32 * a20 + b33 * a30
	dest[13] = b30 * a01 + b31 * a11 + b32 * a21 + b33 * a31
	dest[14] = b30 * a02 + b31 * a12 + b32 * a22 + b33 * a32
	dest[15] = b30 * a03 + b31 * a13 + b32 * a23 + b33 * a33

	return dest

def mat4_multiplyVec3(mat, vec, dest):

	if (None==dest):
		dest = vec
	
	x = vec[0]
	y = vec[1]
	z = vec[2]

	dest[0] = mat[0] * x + mat[4] * y + mat[8] * z + mat[12]
	dest[1] = mat[1] * x + mat[5] * y + mat[9] * z + mat[13]
	dest[2] = mat[2] * x + mat[6] * y + mat[10] * z + mat[14]

	return dest

def mat4_multiplyVec4(mat, vec, dest):

	if (None==dest):
		dest = vec
	
	x = vec[0] 
	y = vec[1]
	z = vec[2] 
	w = vec[3]

	dest[0] = mat[0] * x + mat[4] * y + mat[8] * z + mat[12] * w
	dest[1] = mat[1] * x + mat[5] * y + mat[9] * z + mat[13] * w
	dest[2] = mat[2] * x + mat[6] * y + mat[10] * z + mat[14] * w
	dest[3] = mat[3] * x + mat[7] * y + mat[11] * z + mat[15] * w

	return dest

def mat4_translate(mat, vec, dest):

	x = vec[0]
	y = vec[1]
	z = vec[2]

	if (None==dest or mat == dest):
	
		mat[12] = mat[0] * x + mat[4] * y + mat[8] * z + mat[12]
		mat[13] = mat[1] * x + mat[5] * y + mat[9] * z + mat[13]
		mat[14] = mat[2] * x + mat[6] * y + mat[10] * z + mat[14]
		mat[15] = mat[3] * x + mat[7] * y + mat[11] * z + mat[15]
		
		return mat

	a00 = mat[0]
	a01 = mat[1]
	a02 = mat[2]
	a03 = mat[3]
	a10 = mat[4]
	a11 = mat[5]
	a12 = mat[6]
	a13 = mat[7]
	a20 = mat[8]
	a21 = mat[9]
	a22 = mat[10]
	a23 = mat[11]

	dest[0] = a00
	dest[1] = a01
	dest[2] = a02
	dest[3] = a03
	dest[4] = a10
	dest[5] = a11
	dest[6] = a12
	dest[7] = a13
	dest[8] = a20
	dest[9] = a21
	dest[10] = a22
	dest[11] = a23

	dest[12] = a00 * x + a10 * y + a20 * z + mat[12]
	dest[13] = a01 * x + a11 * y + a21 * z + mat[13]
	dest[14] = a02 * x + a12 * y + a22 * z + mat[14]
	dest[15] = a03 * x + a13 * y + a23 * z + mat[15]
	
	return dest

def mat4_scale(mat, vec, dest):

	x = vec[0]
	y = vec[1]
	z = vec[2]

	if (None==dest or mat == dest):
	
		mat[0]  = mat[0]  * x
		mat[1]  = mat[1]  * x
		mat[2]  = mat[2]  * x
		mat[3]  = mat[3]  * x
		mat[4]  = mat[4]  * y
		mat[5]  = mat[5]  * y
		mat[6]  = mat[6]  * y
		mat[7]  = mat[7]  * y
		mat[8]  = mat[8]  * z
		mat[9]  = mat[9]  * z
		mat[10] = mat[10] * z
		mat[11] = mat[11] * z
		
		return mat
	
	dest[0] = mat[0] * x
	dest[1] = mat[1] * x
	dest[2] = mat[2] * x
	dest[3] = mat[3] * x
	dest[4] = mat[4] * y
	dest[5] = mat[5] * y
	dest[6] = mat[6] * y
	dest[7] = mat[7] * y
	dest[8] = mat[8] * z
	dest[9] = mat[9] * z
	dest[10] = mat[10] * z
	dest[11] = mat[11] * z
	dest[12] = mat[12]
	dest[13] = mat[13]
	dest[14] = mat[14]
	dest[15] = mat[15]
	
	return dest

def mat4_rotate(mat, angle, axis, dest):

	x = axis[0]
	y = axis[1]
	z = axis[2]
	len = sqrt(x * x + y * y + z * z)

	if (None==len):
	
		return None
	
	if (len != 1):
	
		len = 1 / len
		x = x * len
		y = y * len
		z = z * len
	
	s = sin(angle)
	c = cos(angle)
	t = 1 - c

	a00 = mat[0]
	a01 = mat[1]
	a02 = mat[2]
	a03 = mat[3]
	a10 = mat[4]
	a11 = mat[5]
	a12 = mat[6]
	a13 = mat[7]
	a20 = mat[8]
	a21 = mat[9]
	a22 = mat[10]
	a23 = mat[11]

	#Construct the elements of the rotation matrix
	b00 = x * x * t + c
	b01 = y * x * t + z * s
	b02 = z * x * t - y * s
	b10 = x * y * t - z * s
	b11 = y * y * t + c
	b12 = z * y * t + x * s
	b20 = x * z * t + y * s
	b21 = y * z * t - x * s
	b22 = z * z * t + c

	if (None==dest):
		dest = mat
	
	elif (mat != dest):  	#If the source and destination differ, copy the unchanged last row
		dest[12] = mat[12]
		dest[13] = mat[13]
		dest[14] = mat[14]
		dest[15] = mat[15]
	
	#Perform rotation-specific matrix multiplication
	dest[0] = a00 * b00 + a10 * b01 + a20 * b02
	dest[1] = a01 * b00 + a11 * b01 + a21 * b02
	dest[2] = a02 * b00 + a12 * b01 + a22 * b02
	dest[3] = a03 * b00 + a13 * b01 + a23 * b02

	dest[4] = a00 * b10 + a10 * b11 + a20 * b12
	dest[5] = a01 * b10 + a11 * b11 + a21 * b12
	dest[6] = a02 * b10 + a12 * b11 + a22 * b12
	dest[7] = a03 * b10 + a13 * b11 + a23 * b12

	dest[8] = a00 * b20 + a10 * b21 + a20 * b22
	dest[9] = a01 * b20 + a11 * b21 + a21 * b22
	dest[10] = a02 * b20 + a12 * b21 + a22 * b22
	dest[11] = a03 * b20 + a13 * b21 + a23 * b22
	
	return dest

def mat4_rotateX(mat, angle, dest):

	s = sin(angle)
	c = cos(angle)
	a10 = mat[4]
	a11 = mat[5]
	a12 = mat[6]
	a13 = mat[7]
	a20 = mat[8]
	a21 = mat[9]
	a22 = mat[10]
	a23 = mat[11]

	if (None==dest):
		dest = mat
	
	elif (mat != dest):  	#If the source and destination differ, copy the unchanged rows
	
		dest[0] = mat[0]
		dest[1] = mat[1]
		dest[2] = mat[2]
		dest[3] = mat[3]

		dest[12] = mat[12]
		dest[13] = mat[13]
		dest[14] = mat[14]
		dest[15] = mat[15]
	
	#Perform axis-specific matrix multiplication
	dest[4] = a10 * c + a20 * s
	dest[5] = a11 * c + a21 * s
	dest[6] = a12 * c + a22 * s
	dest[7] = a13 * c + a23 * s

	dest[8] = a10 * -s + a20 * c
	dest[9] = a11 * -s + a21 * c
	dest[10] = a12 * -s + a22 * c
	dest[11] = a13 * -s + a23 * c
	return dest

def mat4_rotateY(mat, angle, dest):

	s = sin(angle)
	c = cos(angle)
	a00 = mat[0]
	a01 = mat[1]
	a02 = mat[2]
	a03 = mat[3]
	a20 = mat[8]
	a21 = mat[9]
	a22 = mat[10]
	a23 = mat[11]

	if (None==dest):
		dest = mat
	
	elif (mat != dest):  	#If the source and destination differ, copy the unchanged rows
	
		dest[4] = mat[4]
		dest[5] = mat[5]
		dest[6] = mat[6]
		dest[7] = mat[7]

		dest[12] = mat[12]
		dest[13] = mat[13]
		dest[14] = mat[14]
		dest[15] = mat[15]
	
	#Perform axis-specific matrix multiplication
	dest[0] = a00 * c + a20 * -s
	dest[1] = a01 * c + a21 * -s
	dest[2] = a02 * c + a22 * -s
	dest[3] = a03 * c + a23 * -s

	dest[8] = a00 * s + a20 * c
	dest[9] = a01 * s + a21 * c
	dest[10] = a02 * s + a22 * c
	dest[11] = a03 * s + a23 * c
	
	return dest

def mat4_rotateZ(mat, angle, dest):
	s = sin(angle)
	c = cos(angle)
	a00 = mat[0]
	a01 = mat[1]
	a02 = mat[2]
	a03 = mat[3]
	a10 = mat[4] 
	a11 = mat[5] 
	a12 = mat[6] 
	a13 = mat[7]

	if (None==dest):
		dest = mat
	
	elif (mat != dest):  	#If the source and destination differ, copy the unchanged last row
		dest[8] = mat[8]
		dest[9] = mat[9]
		dest[10] = mat[10]
		dest[11] = mat[11]

		dest[12] = mat[12]
		dest[13] = mat[13]
		dest[14] = mat[14]
		dest[15] = mat[15]
	
	#Perform axis-specific matrix multiplication
	dest[0] = a00 * c + a10 * s
	dest[1] = a01 * c + a11 * s
	dest[2] = a02 * c + a12 * s
	dest[3] = a03 * c + a13 * s

	dest[4] = a00 * -s + a10 * c
	dest[5] = a01 * -s + a11 * c
	dest[6] = a02 * -s + a12 * c
	dest[7] = a03 * -s + a13 * c

	return dest

def mat4_frustum(left, right, bottom, top, near, far, dest):

	if (None==dest):
		dest = mat4_create(None)
	
	rl = (right - left) 
	tb = (top - bottom) 
	fn = (far - near)
	
	dest[0] = (near * 2) / rl
	dest[1] = 0
	dest[2] = 0
	dest[3] = 0
	dest[4] = 0
	dest[5] = (near * 2) / tb
	dest[6] = 0
	dest[7] = 0
	dest[8] = (right + left) / rl
	dest[9] = (top + bottom) / tb
	dest[10] = -(far + near) / fn
	dest[11] = -1
	dest[12] = 0
	dest[13] = 0
	dest[14] = -(far * near * 2) / fn
	dest[15] = 0
	
	return dest

def mat4_perspective(fovy, aspect, near, far, dest):

	top = near * tan(fovy * 3.14159265358979323846 / 360.0)
	right = top * aspect
	
	return mat4_frustum(-right, right, -top, top, near, far, dest)

def mat4_ortho(left, right, bottom, top, near, far, dest):

	if (None==dest):
		dest = mat4_create(None)
	
	rl = (right - left) 
	tb = (top - bottom) 
	fn = (far - near)
	
	dest[0] = 2 / rl
	dest[1] = 0
	dest[2] = 0
	dest[3] = 0
	dest[4] = 0
	dest[5] = 2 / tb
	dest[6] = 0
	dest[7] = 0
	dest[8] = 0
	dest[9] = 0
	dest[10] = -2 / fn
	dest[11] = 0
	dest[12] = -(left + right) / rl
	dest[13] = -(top + bottom) / tb
	dest[14] = -(far + near) / fn
	dest[15] = 1
	
	return dest

def mat4_ortho_GetExtent(dest):
	
	left = 0.0
	right = 0.0
	bottom = 0.0
	top = 0.0
		
	if None != dest :
		right = (1.0 - dest[12])/dest[0]
		
		left = right - (2.0/dest[0])
		
		top =  (1.0 - dest[13])/dest[5]
		
		bottom = top - (2.0/dest[5])
		
		far = (dest[14] - 1.0)/dest[10]
		
		near = far + (2.0/dest[10])
	
	return left, right, bottom, top, far, near
	
def mat4_lookAt(eye, center, up, dest):

	if (None==dest):
		dest = mat4_create(None)
	
	eyex = eye[0]
	eyey = eye[1]
	eyez = eye[2]
	upx = up[0]
	upy = up[1]
	upz = up[2]
	centerx = center[0]
	centery = center[1]
	centerz = center[2]

	if (eyex == centerx and eyey == centery and eyez == centerz):
		return mat4_identity(dest)
	
	#vec3.direction(eye, center, z)
	z0 = eyex - centerx
	z1 = eyey - centery
	z2 = eyez - centerz

	#normalize (no check needed for 0 because of early return)
	len = 1 / sqrt(z0 * z0 + z1 * z1 + z2 * z2)
	z0 = z0 * len
	z1 = z1 * len
	z2 = z2 * len

	#vec3.normalize(vec3.cross(up, z, x))
	x0 = upy * z2 - upz * z1
	x1 = upz * z0 - upx * z2
	x2 = upx * z1 - upy * z0
	len = sqrt(x0 * x0 + x1 * x1 + x2 * x2)
	
	if (None==len):
		x0 = 0
		x1 = 0
		x2 = 0
	
	else:
		len = 1 / len
		x0 = x0 * len
		x1 = x1 * len
		x2 = x2 * len

	#vec3.normalize(vec3.cross(z, x, y))
	y0 = z1 * x2 - z2 * x1
	y1 = z2 * x0 - z0 * x2
	y2 = z0 * x1 - z1 * x0

	len = sqrt(y0 * y0 + y1 * y1 + y2 * y2)
	
	if (None==len):
		y0 = 0
		y1 = 0
		y2 = 0
	
	else:
		len = 1 / len
		y0 = y0 * len
		y1 = y1 * len
		y2 = y2 * len
	
	dest[0] = x0
	dest[1] = y0
	dest[2] = z0
	dest[3] = 0
	dest[4] = x1
	dest[5] = y1
	dest[6] = z1
	dest[7] = 0
	dest[8] = x2
	dest[9] = y2
	dest[10] = z2
	dest[11] = 0
	dest[12] = -(x0 * eyex + x1 * eyey + x2 * eyez)
	dest[13] = -(y0 * eyex + y1 * eyey + y2 * eyez)
	dest[14] = -(z0 * eyex + z1 * eyey + z2 * eyez)
	dest[15] = 1

	return dest

def mat4_fromRotationTranslation(quat, vec, dest):

	if (None==dest):
		dest = mat4_create(None)
	
	#Quaternion math
	x = quat[0] 
	y = quat[1] 
	z = quat[2] 
	w = quat[3]
	x2 = x + x
	y2 = y + y
	z2 = z + z
	xx = x * x2
	xy = x * y2
	xz = x * z2
	yy = y * y2
	yz = y * z2 
	zz = z * z2 
	wx = w * x2 
	wy = w * y2 
	wz = w * z2

	dest[0] = 1 - (yy + zz)
	dest[1] = xy + wz
	dest[2] = xz - wy
	dest[3] = 0
	dest[4] = xy - wz
	dest[5] = 1 - (xx + zz)
	dest[6] = yz + wx
	dest[7] = 0
	dest[8] = xz + wy
	dest[9] = yz - wx
	dest[10] = 1 - (xx + yy)
	dest[11] = 0
	dest[12] = vec[0]
	dest[13] = vec[1]
	dest[14] = vec[2]
	dest[15] = 1

	return dest

################################################################################

def quat_create(quat):

	dest = [0.0]*4

	if (quat):
		dest[0] = quat[0]
		dest[1] = quat[1]
		dest[2] = quat[2]
		dest[3] = quat[3]
	
	return dest

def quat_set(quat, dest):

	dest[0] = quat[0]
	dest[1] = quat[1]
	dest[2] = quat[2]
	dest[3] = quat[3]

	return dest

def quat_calculateW(quat, dest):

	x = quat[0]
	y = quat[1]
	z = quat[2]

	if (None==dest or quat == dest):
		quat[3] = -sqrt(fabs(1.0 - x * x - y * y - z * z))
		
		return quat
	
	dest[0] = x
	dest[1] = y
	dest[2] = z
	dest[3] = -sqrt(fabs(1.0 - x * x - y * y - z * z))
	
	return dest

def quat_dot(quat, quat2):

	return quat[0] * quat2[0] + quat[1] * quat2[1] + quat[2] * quat2[2] + quat[3] * quat2[3]

def quat_inverse(quat, dest):

	dot = quat_dot(quat, quat)
	
	invDot = 1.0 / dot
	
	if (None==dest or quat == dest):
	
		quat[0] = quat[0] * -invDot
		quat[1] = quat[1] * -invDot
		quat[2] = quat[2] * -invDot
		quat[3] = quat[3] * invDot
		
		return quat
	
	dest[0] = -quat[0] * invDot
	dest[1] = -quat[1] * invDot
	dest[2] = -quat[2] * invDot
	dest[3] = quat[3] * invDot
	
	return dest

def quat_conjugate(quat, dest):

	if (None==dest or quat == dest):
	
		quat[0] = quat[0] * -1
		quat[1] = quat[1] * -1
		quat[2] = quat[2] * -1
		
		return quat
	
	dest[0] = -quat[0]
	dest[1] = -quat[1]
	dest[2] = -quat[2]
	dest[3] = quat[3]
	
	return dest

def quat_length(quat):

	x = quat[0]
	y = quat[1]
	z = quat[2]
	w = quat[3]
	
	return sqrt(x * x + y * y + z * z + w * w)

# Quaternions always obey:  a^2 + b^2 + c^2 + d^2 = 1.0
# If they don't add up to 1.0, dividing by their magnitued will
# renormalize them.
# 
# Note: See the following for more information on quaternions:
# 
# - Shoemake, K., Animating rotation with quaternion curves, Computer
#   Graphics 19, No 3 (Proc. SIGGRAPH'85), 245-254, 1985.
# - Pletinckx, D., Quaternion calculus as a basic tool in computer
#   graphics, The Visual Computer 5, 2-13, 1989.
#
def quat_normalize(quat, dest):

	if (None == dest):
		dest = quat
	
	x = quat[0]
	y = quat[1]
	z = quat[2]
	w = quat[3]
	
	len = sqrt(x * x + y * y + z * z + w * w)
	
	if (len == 0):
	
		dest[0] = 0
		dest[1] = 0
		dest[2] = 0
		dest[3] = 0
		
		return dest
	
	len = 1 / len
	dest[0] = x * len
	dest[1] = y * len
	dest[2] = z * len
	dest[3] = w * len

	return dest

def quat_multiply(quat, quat2, dest):

	if (None==dest):
		dest = quat
	
	qax = quat[0] 
	qay = quat[1] 
	qaz = quat[2] 
	qaw = quat[3]
	qbx = quat2[0] 
	qby = quat2[1] 
	qbz = quat2[2] 
	qbw = quat2[3]

	dest[0] = qax * qbw + qaw * qbx + qay * qbz - qaz * qby
	dest[1] = qay * qbw + qaw * qby + qaz * qbx - qax * qbz
	dest[2] = qaz * qbw + qaw * qbz + qax * qby - qay * qbx
	dest[3] = qaw * qbw - qax * qbx - qay * qby - qaz * qbz

	return dest

def quat_multiplyVec3(quat, vec, dest):

	if (None==dest):
		dest = vec
	
	x = vec[0]
	y = vec[1]
	z = vec[2]
	qx = quat[0]
	qy = quat[1] 
	qz = quat[2]
	qw = quat[3]
	#calculate quat * vec
	ix = qw * x + qy * z - qz * y
	iy = qw * y + qz * x - qx * z
	iz = qw * z + qx * y - qy * x 
	iw = -qx * x - qy * y - qz * z

	#calculate result * inverse quat
	dest[0] = ix * qw + iw * -qx + iy * -qz - iz * -qy
	dest[1] = iy * qw + iw * -qy + iz * -qx - ix * -qz
	dest[2] = iz * qw + iw * -qz + ix * -qy - iy * -qx

	return dest

def quat_toMat3(quat, dest):

	if (None==dest):
		dest = mat3_create(None)
	
	x = quat[0] 
	y = quat[1] 
	z = quat[2] 
	w = quat[3]
	x2 = x + x
	y2 = y + y
	z2 = z + z
	xx = x * x2
	xy = x * y2
	xz = x * z2
	yy = y * y2
	yz = y * z2 
	zz = z * z2 
	wx = w * x2 
	wy = w * y2 
	wz = w * z2

	dest[0] = 1 - (yy + zz)
	dest[1] = xy + wz
	dest[2] = xz - wy

	dest[3] = xy - wz
	dest[4] = 1 - (xx + zz)
	dest[5] = yz + wx

	dest[6] = xz + wy
	dest[7] = yz - wx
	dest[8] = 1 - (xx + yy)

	return dest

def quat_toMat4_do_not_use_directly(quat, dest):

	if (None==dest):
		dest = mat4_create(None)
	
	x = quat[0]
	y = quat[1]
	z = quat[2]
	w = quat[3]
	
	x2 = x + x
	y2 = y + y
	z2 = z + z
	
	xx = x * x2
	xy = x * y2
	xz = x * z2
	
	yy = y * y2
	yz = y * z2 
	zz = z * z2 
	
	wx = w * x2 
	wy = w * y2 
	wz = w * z2

	dest[0] = 1 - (yy + zz)
	dest[1] = xy + wz
	dest[2] = xz - wy
	dest[3] = 0

	dest[4] = xy - wz
	dest[5] = 1 - (xx + zz)
	dest[6] = yz + wx
	dest[7] = 0

	dest[8] = xz + wy
	dest[9] = yz - wx
	dest[10] = 1 - (xx + yy)
	dest[11] = 0

	dest[12] = 0
	dest[13] = 0
	dest[14] = 0
	dest[15] = 1

	return dest

def quat_slerp(quat, quat2, slerp, dest):

	if (None==dest):
	
		dest = quat
	
	cosHalfTheta = quat[0] * quat2[0] + quat[1] * quat2[1] + quat[2] * quat2[2] + quat[3] * quat2[3]

	if (fabs(cosHalfTheta) >= 1.0):
	
		if (dest != quat):
		
			dest[0] = quat[0]
			dest[1] = quat[1]
			dest[2] = quat[2]
			dest[3] = quat[3]
		
		return dest
	
	halfTheta = acos(cosHalfTheta)
	sinHalfTheta = sqrt(1.0 - cosHalfTheta * cosHalfTheta)

	if (fabs(sinHalfTheta) < 0.001):
	
		dest[0] = (quat[0] * 0.5 + quat2[0] * 0.5)
		dest[1] = (quat[1] * 0.5 + quat2[1] * 0.5)
		dest[2] = (quat[2] * 0.5 + quat2[2] * 0.5)
		dest[3] = (quat[3] * 0.5 + quat2[3] * 0.5)
		return dest
	
	ratioA = sin((1 - slerp) * halfTheta) / sinHalfTheta
	ratioB = sin(slerp * halfTheta) / sinHalfTheta

	dest[0] = (quat[0] * ratioA + quat2[0] * ratioB)
	dest[1] = (quat[1] * ratioA + quat2[1] * ratioB)
	dest[2] = (quat[2] * ratioA + quat2[2] * ratioB)
	dest[3] = (quat[3] * ratioA + quat2[3] * ratioB)

	return dest

################################################################################

def gl_mat4_multiply(matb, mata, retMat4):
	#retMat4 = mat4_create(None)
	mat4_multiply(mata, matb, retMat4)
	return retMat4
	
def gl_quat_from_x_rotation(theta):
	thetaBy2 = theta * 0.5
	
	dest = quat_create(None)
	dest[0] = sin(thetaBy2)
	dest[3] = cos(thetaBy2)
	
	return dest
	
def gl_quat_from_y_rotation(theta):
	thetaBy2 = theta * 0.5
	
	dest = quat_create(None)
	dest[1] = sin(thetaBy2)
	dest[3] = cos(thetaBy2)
	
	return dest
	
def gl_quat_from_z_rotation(theta):
	thetaBy2 = theta * 0.5
	
	dest = quat_create(None)
	dest[2] = sin(thetaBy2)
	dest[3] = cos(thetaBy2)
	
	return dest

################################################

def gl_mat4_from_translation(location_v):
	location_m = mat4_identity(None)
	mat4_translate(location_m, location_v, None)
	return location_m
		
def gl_mat4_from_quat(q, dest):
	quat_toMat4_do_not_use_directly(q, dest)
	#mat4_transpose(dest, None)
	
def gl_mat4_from_scale(scale_v):
	scale_m = mat4_identity(None)
	mat4_scale(scale_m, scale_v, None)
	return scale_m
	
################################################################################

# Additional helpers

# Ref: https://github.com/Kazade/kazmath

# Rotates a quaternion around an axis
def quat_rot_from_axisangle(axis, theta, dest):
	thetaBy2 = theta * 0.5

	dest[0] = axis[0] * sin(thetaBy2)
	dest[1] = axis[1] * sin(thetaBy2)
	dest[2] = axis[2] * sin(thetaBy2)
	dest[3] = cos(thetaBy2)

	quat_normalize(dest, None)

	return dest

# Build a rotation matrix from an axis and an angle.
def mat4_rot_from_axisangle(axis, theta):
	q = quat_create(None)
	quat_rot_from_axisangle(axis, theta, q)
	
	dest = mat4_create(None)
	gl_mat4_from_quat(q, dest)

	return dest
	
def mat4_extract_translation(matm, dest):
	dest[0] = matm[12]
	dest[1] = matm[13]
	dest[2] = matm[14]

	return dest
	
def quat_from_mat4(iMat):
	
	# Ref: https://www.j3d.org/matrix_faq/matrfaq_latest.html
	# Q55.  How do I convert a rotation matrix to a quaternion?
	# But, before that refer matrix order used in described algorithm
	# I1.  Important note relating to OpenGL and this document
	#
	#	Algorithm                  OpenGL
	#        | 0  1  2  3  |            | 0  4  8  12 |
	#        |             |            |             |
	#        | 4  5  6  7  |            | 1  5  9  13 |
	#    M = |             |        M = |             |
	#        | 8  9  10 11 |            | 2  6  10 14 |
	#        |             |            |             |
	#        | 12 13 14 15 |            | 3  7  11 15 |
	#
	#
	# Implementation below uses OpenGL order
	
	q = quat_create(None)
	
	x = 0.0
	y = 0.0
	z = 0.0
	w = 0.0
	
	diagonal = iMat[0] + iMat[5] + iMat[10] + 1
	if(diagonal > sys.float_info.epsilon) :
		# Calculate the scale of the diagonal
		scale = sqrt(diagonal) * 2.0

		# Calculate the x, y, x and w of the quaternion through the respective equation
		x = ( iMat[6] - iMat[9] ) / scale
		y = ( iMat[8] - iMat[2] ) / scale
		z = ( iMat[1] - iMat[4] ) / scale
		w = 0.25 * scale
	
	else :
		# If the first element of the diagonal is the greatest value
		if ( iMat[0] > iMat[5] and iMat[0] > iMat[10] ) :
			# Find the scale according to the first element, and double that value
			scale = sqrt( 1.0 + iMat[0] - iMat[5] - iMat[10] ) * 2.0

			# Calculate the x, y, x and w of the quaternion through the respective equation
			x = 0.25 * scale
			y = (iMat[1] + iMat[4] ) / scale
			z = (iMat[8] + iMat[2] ) / scale
			w = (iMat[6] - iMat[9] ) / scale
		
		# Else if the second element of the diagonal is the greatest value
		elif (iMat[5] > iMat[10]) :
			# Find the scale according to the second element, and double that value
			scale = sqrt( 1.0 + iMat[5] - iMat[0] - iMat[10] ) * 2.0

			# Calculate the x, y, x and w of the quaternion through the respective equation
			x = (iMat[1] + iMat[4] ) / scale
			y = 0.25 * scale
			z = (iMat[6] + iMat[9] ) / scale
			w = (iMat[8] - iMat[2] ) / scale
		
		# Else the third element of the diagonal is the greatest value
		else :
			# Find the scale according to the third element, and double that value
			scale  = sqrt( 1.0 + iMat[10] - iMat[0] - iMat[5] ) * 2.0

			# Calculate the x, y, x and w of the quaternion through the respective equation
			x = (iMat[8] + iMat[2] ) / scale
			y = (iMat[6] + iMat[9] ) / scale
			z = 0.25 * scale
			w = (iMat[1] - iMat[4] ) / scale
	
	q[0] = x
	q[1] = y
	q[2] = z
	q[3] = w
	
	return q
	
def mat4_decompose(iMat):
	
	# From mvMatrix, obtain T R S values
	
	#
	translation_v = vec3_create([iMat[12], iMat[13], iMat[14]])
	
	#
	
	scale_x = vec3_length([iMat[0], iMat[1], iMat[2]])
	scale_y = vec3_length([iMat[4], iMat[5], iMat[6]])
	scale_z = vec3_length([iMat[8], iMat[9], iMat[10]])			
	scale_v = vec3_create([scale_x, scale_y, scale_z])
	
	#
	
	rotation_m = mat4_identity(None)
	rotation_m[0] = iMat[0]/scale_x
	rotation_m[1] = iMat[1]/scale_x
	rotation_m[2] = iMat[2]/scale_x
	
	rotation_m[4] = iMat[4]/scale_y
	rotation_m[5] = iMat[5]/scale_y
	rotation_m[6] = iMat[6]/scale_y
	
	rotation_m[8] = iMat[8]/scale_z
	rotation_m[9] = iMat[9]/scale_z
	rotation_m[10] = iMat[10]/scale_z	
	
	rotation_v = quat_from_mat4(rotation_m)
	
	return translation_v,rotation_v,scale_v

################################################################################

# Trackball helpers
#
# Copyright (c)  2014 Nicolas Rougier
#                2008 Roger Allen
#                1993, 1994, Silicon Graphics, Inc.
#
# Implementation of a virtual trackball.
# Implemented by Gavin Bell, lots of ideas from Thant Tessman and
# the August '88 issue of Siggraph's "Computer Graphics," pp. 121-129.
#
# Original code from:
# David M. Ciemiewicz, Mark Grossman, Henry Moreton, and Paul Haeberli
#

# Given an axis and angle, compute quaternion.
def axis_to_quat(a, phi, q):
	normalised_a = vec3_create(None)
	vec3_normalize(a, normalised_a)
	
	q[0] = normalised_a[0]
	q[1] = normalised_a[1]
	q[2] = normalised_a[2]
	
	vec3_scale(q, sin(phi/2.0), None)
	
	q[3] = cos(phi/2.0)


# Project an x,y pair onto a sphere of radius r OR a hyperbolic sheet
# if we are away from the center of the sphere.
def tb_project_to_sphere(r, x, y):
	d = sqrt(x*x + y*y)

	if d < (r * 0.70710678118654752440) :
		# Inside sphere 
		z = sqrt(r*r - d*d)
	else :
		# On hyperbola 
		t = r / 1.41421356237309504880
		z = t*t / d

	return z
   
# Given two rotations, e1 and e2, expressed as quaternion rotations,
# figure out the equivalent single rotation and stuff it into dest.
# 
# This routine also normalizes the result every RENORMCOUNT times it is
# called, to keep error from creeping in.
# 
# NOTE: This routine is written so that q1 or q2 may be the same
# as dest (or each other).
# 
RENORMCOUNT=97
def add_quats(q1, q2, dest, renormcounter):    
    t1 = quat_create(q1) 
    t2 = quat_create(q2)  
    t3 = quat_create(None) 
    tf = quat_create(None) 
    
    # Note: using vec3 fxn on quat
    vec3_scale(t1, q2[3], None)
    
    # Note: using vec3 fxn on quat
    vec3_scale(t2, q1[3], None)
    
    # Note: using vec3 fxn on quat
    vec3_cross(q2, q1, t3)
    
    # Note: using vec3 fxn on quat
    vec3_add(t1, t2, tf)
    
    # Note: using vec3 fxn on quat
    vec3_add(t3, tf, tf)
    
    d1_dot_q2_using_vec3_dot = vec3_dot(q1, q2)
    tf[3] = q1[3] * q2[3] - d1_dot_q2_using_vec3_dot

    dest[0] = tf[0]
    dest[1] = tf[1]
    dest[2] = tf[2]
    dest[3] = tf[3]

    if (++renormcounter > RENORMCOUNT):
        renormcounter = 0
        quat_normalize(dest, None)
   

# This size should really be based on the distance from the center of
# rotation to the point on the object underneath the mouse.  That
# point would then track the mouse as closely as possible.  This is a
# simple example, though, so that is left as an Exercise for the
# Programmer.
TRACKBALLSIZE=0.8

# Ok, simulate a track-ball.  Project the points onto the virtual
# trackball, then figure out the axis of rotation, which is the cross
# product of P1 P2 and O P1 (O is the center of the ball, 0,0,0)
# Note:  This is a deformed trackball-- is a trackball in the center,
# but is deformed into a hyperbolic sheet of rotation away from the
# center.  This particular function was chosen after trying out
# several variations.
# 
# It is assumed that the arguments to this routine are in the range
# (-1.0 ... 1.0)
# 

def trackball(q, p1x, p1y, p2x, p2y):
	p1 = vec3_create(None) 
	p2 = vec3_create(None)
	
	# Axis of rotation 
	a = vec3_create(None) 
	d = vec3_create(None)

	if (p1x == p2x) and (p1y == p2y) :
		# Zero rotation 
		q[0] = 0.0
		q[1] = 0.0
		q[2] = 0.0
		q[3] = 1.0
		
		return

	# First, figure out z-coordinates for projection of P1 and P2 to
	# deformed sphere 
	p1[0] = p1x
	p1[1] = p1y 
	p1[2] = tb_project_to_sphere(TRACKBALLSIZE, p1x, p1y)

	p2[0] = p2x 
	p2[1] = p2y 
	p2[2] = tb_project_to_sphere(TRACKBALLSIZE, p2x, p2y)

	# Now, we want the cross product of P1 and P2
	vec3_cross(p2, p1, a)

	# Figure out how much to rotate around that axis.
	vec3_subtract(p1, p2, d)
	t = vec3_length(d) / (2.0*TRACKBALLSIZE)

	# Avoid problems with out-of-control values...
	if t > 1.0 :
		t = 1.0

	if t < -1.0 :
		t = -1.0

	# how much to rotate about axis
	phi = 2.0 * asin(t)

	axis_to_quat(a, phi, q)

################################################################################

# Matrix Stack helpers

class matstack:
	def __init__(self):
		self.entries = []

	def isEmpty(self):
		return self.entries == []

	def push(self, item):
		self.entries.append(item)

	def pop(self):
		
		if 0 < self.size() :
			return self.entries.pop()
			
		else:
			print("Expected stack pop is already empty.")

	def peek(self):
		if 0 < self.size() :
			return self.entries[len(self.entries)-1]
		else:
			return None

	def size(self):
		return len(self.entries)
		
	##############################################################################
		
	def loadMatrix(self, m):
		m_Tmp = mat4_create(m)
		self.push(m_Tmp)
		
	def unload(self):
		self.entries.clear()		
		
	def loadIdentityMatrix(self):
		m_Id = mat4_identity(None)
		self.loadMatrix(m_Id)		
		
	def multMatrix(self, m):
		if 0 < self.size() :
			m_Top = self.peek()
			m_Tmp = mat4_create(None)
			gl_mat4_multiply(m, m_Top, m_Tmp)
			mat4_set(m_Tmp, m_Top)
		
	def getMatrix(self, dest):
		if 0 < self.size() :
			m_Top = self.peek()
			mat4_set(m_Top, dest)
			
	def pushMatrix(self):
		if 0 < self.size() :
			m_Top = self.peek()
			self.loadMatrix(m_Top)
		
	def popMatrix(self):
		if 0 < self.size() :
			self.pop()
			
	def replaceTop(self, m):
		if 0 < self.size() :
			m_Top = self.peek()
			mat4_set(m , m_Top)
		
	def copyTop(self, m):
		if 0 < self.size() :
			m_Top = self.peek()
			mat4_set(m_Top, m)
