import numpy as np
import cupy as cp
from biotsavartlaw import BiotSavartLaw
import time
import matplotlib.pyplot as plt
from currentgenerator import CurrentGen

#create a mesh -- if mesh is too dense, quiver will die
meshDense = 10
width = 10
length = 10
height = 10
x = cp.linspace(-width, width, meshDense)
y = cp.linspace(-length, length, meshDense)
z = cp.linspace(-height, height, meshDense)

X, Y, Z = cp.meshgrid(x, y, z, indexing='ij')
r = cp.stack([X, Y, Z], axis=-1).reshape(-1, 3)

current = CurrentGen()  #make current polygon
dLArray = cp.zeros((0, 7), dtype=cp.float32)

line1start = cp.array([-10, 0, 0], dtype=cp.float32)
line1end = cp.array([10, 0, 0], dtype=cp.float32)
dLArray = cp.append(dLArray, current.getLineCurrent(line1start, line1end, I=1), axis=0)
# line2start = cp.array([0, 0, 0], dtype=cp.float32)
# line2end = cp.array([0, -10, 0], dtype=cp.float32)
# dLArray = cp.append(dLArray, current.getLineCurrent(line2start, line2end, I=100), axis=0)
origin = cp.array([-8, 0, 0], dtype=cp.float32)
face = cp.array([1, 0, 0], dtype=cp.float32)
dLArray = cp.append(dLArray, current.getCircleCurrent(origin, face, radius=5, I=1, dense=50), axis=0)
origin2 = cp.array([8, 0, 0], dtype=cp.float32)
face2 = cp.array([1, 0, 0], dtype=cp.float32)
dLArray = cp.append(dLArray, current.getCircleCurrent(origin2, face2, radius=5, I=1, dense=50), axis=0)
MFCalc = BiotSavartLaw()

#execution of biotsavart law system
MF = cp.zeros((meshDense**3, 3))
for l in dLArray:
    tempr = r - l[0:3]
    MF += MFCalc.getMagneticField(I=l[6], dL=l[3:6], r=tempr)


#execution quiver
grim = plt.figure().add_subplot(projection='3d')
plotMF = cp.asnumpy(MF)
plotr = cp.asnumpy(r)
plotMF_maxnorm = float(cp.max(cp.linalg.norm(MF, axis=1)))
maxArrowLen = width/2
grim.quiver(plotr[:, 0], plotr[:, 1], plotr[:, 2], 
            plotMF[:, 0], plotMF[:, 1], plotMF[:, 2], 
            color='blue', length=maxArrowLen/plotMF_maxnorm)

plotdLArray = cp.asnumpy(dLArray)
grim.quiver(plotdLArray[:, 0], plotdLArray[:,1], plotdLArray[:,2], 
            plotdLArray[:,3], plotdLArray[:,4], plotdLArray[:,5], 
            color='red')
grim.set_xlabel("X")
grim.set_xlim(-width, width)
grim.set_ylabel("Y")
grim.set_ylim(-length, length)
grim.set_zlabel("Z")
grim.set_zlim(-height, height)

cp.savetxt('plotr_save.txt', plotr)
cp.savetxt('MF_save.txt', MF)

plt.show()