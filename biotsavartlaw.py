import numpy as np
import cupy as cp

class BiotSavartLaw:
    C = 10^-7   #coefficient
    def __init__(self, muT=1):
        self.muT = muT
    
    def getMagneticField(self, I:float, dL:cp.ndarray, r:cp.ndarray, muT=1):
        #I must be one float value
        #dL must be one row vector
        #r must be set of row vectors
        self.muT = muT
        num = int(r.shape[0])
        norm_r = cp.linalg.norm(r, axis=1).reshape(num, 1)
        unit_r = r/norm_r
        unit_r[cp.isnan(unit_r)] = 0
        result = cp.cross(dL, unit_r)
        result /= norm_r
        result[cp.isnan(result)] = 0
        result /= norm_r
        result[cp.isnan(result)] = 0
        result *= I * self.muT * self.C
        result[cp.isnan(result)] = 0
        result *= -1    #dont know why, but value is opposite...
        return result
    