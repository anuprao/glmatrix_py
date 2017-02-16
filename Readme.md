# glmatrix python version

This is a port of gl-matrix.c (https://github.com/coreh/gl-matrix.c.git) which is a port of gl-matrix.js (https://github.com/toji/gl-matrix).

I frequently experiment with OpenGL on Desktop and then port the necessary effects to the intended target (Mobile or Web). As a result, I find myself shuffling 
with different libraries while comparing the outputs. One such pain point has been the *Matrix related Math* functions. I have great respect for Kazmath, GLM 
and Pyrr which are my tools of choice. While each has their own strengths, I was interested in a light weight implementation suitable for prototyping. A single 
implementation ported across platforms to ease my routine.

gl-matrix.js was my choice for WebGL related work and I was thrilled to find the C version. Since a python version could not be found readily, I hacked my way 
into the night. 


Usage is straightforward, drop in glmatrix.py in your project and just include one the following lines

> import glmatrix
>

or,

> from glmatrix import *
>

An example *example_using_glmatrix.py* is provided to get a hang of the usage.
A reference example with identical output using the wonderful Pyrr() library is also provided.

Remember, while this works, it might still have bugs. Do report an issues you find.
