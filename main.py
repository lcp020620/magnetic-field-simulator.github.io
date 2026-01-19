import cupy as cp
import numpy as np
import matplotlib.pyplot as plt
from currentgenerator import CurrentGen
from magneticfieldsimulator import MagneticFieldSimulator
from vectorgenerator import VectorGenerator
from vectorgenerator import row
import pandas as pd

#create a mesh -- if mesh is too dense, quiver will die
simulator = MagneticFieldSimulator()
meshDense = 30
width = 10
length = 10
height = 10
r = simulator.makeMesh(dense=meshDense, width=width, length=length, height=height)
activateROI = False
current = CurrentGen()  #make current polygon
#========examples of current generation========#
current.getLineCurrent(start=row(-10, 0, 0), end=row(10, 0, 0), I=1, dense=20)
current.getLineCurrent(start=row(0, 0, 0), end=row(0, -10, 0), I=1, dense=20)
# current.getCircleCurrent(origin=row(-8, 0, 0), face=row(1, 0, 0), radius=15, I=1, dense=50)
current.getCircleCurrent(origin=row(0, 0, 0), face=row(1, 0, 0), radius=5, I=1, dense=50)
dLArray = current.currentArr
#==============================================#


#execution of biotsavart law system
MF = simulator.makeMF(dLArray=dLArray)
#==============================================#


#filter only near ROI
vecgen = VectorGenerator()
vecgen.line(start=row(-10, 0, 0), end=row(10, 0, 0), dense=30)
# vecgen.circle(origin=row(0, 0, 0), face=row(1, 0, 0), radius=5, dense=30)
ROI = vecgen.vecArray
ROIIdx = simulator.isROI(space=r, ROI=ROI, range=2)
#==============================================#


#execution quiver
grim = plt.figure().add_subplot(projection='3d')
if  activateROI:
    plotMF = cp.asnumpy(MF[ROIIdx, :])
    plotr = cp.asnumpy(r[ROIIdx, :])
else:
    plotMF = cp.asnumpy(MF)
    plotr = cp.asnumpy(r)

csvArray = np.concatenate([plotr[:, 0:3], plotMF[:, 0:3]], axis=1)
#np.savetxt('MFArray.csv', csvArray, delimiter=',')
pdcsvArray = pd.DataFrame(csvArray, columns=['x', 'y', 'z', 'vx', 'vy', 'vz'])
pdcsvArray.to_csv('C:/[git]MagneticFieldSimulator/MFArray.csv', index=False)

# plotMF_maxnorm = float(cp.max(cp.linalg.norm(MF, axis=1)))
# maxArrowLen = 1.5*width/10
# grim.quiver(plotr[:, 0], plotr[:, 1], plotr[:, 2], 
#             plotMF[:, 0], plotMF[:, 1], plotMF[:, 2], 
#             color='blue', length=maxArrowLen/plotMF_maxnorm)

# plotdLArray = cp.asnumpy(dLArray)
# grim.quiver(plotdLArray[:, 0], plotdLArray[:,1], plotdLArray[:,2], 
#             plotdLArray[:,3], plotdLArray[:,4], plotdLArray[:,5], 
#             color='red')
# grim.set_xlabel("X")
# grim.set_xlim(-width, width)
# grim.set_ylabel("Y")
# grim.set_ylim(-length, length)
# grim.set_zlabel("Z")
# grim.set_zlim(-height, height)
# plt.show()