import cupy as cp
import numpy as np
from biotsavartlaw import BiotSavartLaw
from functools import reduce

class MagneticFieldSimulator:
    def __init__(self, muT:float=1):
        self.muT = muT
        self.meshDense = 0
        self.MFCalc = BiotSavartLaw()

    def makeMesh(self, dense:int, width:float, length:float, height:float):
        self.meshDense = dense

        x = cp.linspace(-width, width, dense)
        y = cp.linspace(-length, length, dense)
        z = cp.linspace(-height, height, dense)
        X, Y, Z = cp.meshgrid(x, y, z, indexing='ij')
        self.r = cp.stack([X, Y, Z], axis=-1).reshape(-1, 3)
        self.MF = cp.zeros((self.meshDense**3, 3))
        return self.r
    
    def makeMF(self, dLArray:cp.ndarray, muT:float=1):
        self.muT = muT
        if  int(dLArray.shape[1]) != 7:
            print('dLArray size is not correct!')
            return
        for l in dLArray:
            tempr = self.r - l[0:3]
            self.MF += self.MFCalc.getMagneticField(I=l[6], dL=l[3:6], r=tempr)
        return self.MF

    def isROI(self, space:cp.ndarray, ROI:cp.ndarray, range:float):
        ROIIndex = []
        for _ in ROI:
            tempspace = space[:, 0:3] - _[0:3]
            tempIndex = cp.where(cp.linalg.norm(tempspace, axis=1)<=range)
            ROIIndex.append(tempIndex)
        temp = [t[0] for t in ROIIndex]
        result = reduce(cp.union1d, temp)
        return result