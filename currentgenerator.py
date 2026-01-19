import cupy as cp

class CurrentGen:
    def __init__(self):
        self.currentArr = cp.zeros((0, 7), dtype=cp.float32)

    def getLineCurrent(self, start:cp.ndarray, end:cp.ndarray, I, dense=10):
        L = end - start
        dL = L/dense
        result = cp.zeros((dense, 7), dtype=cp.float32)
        result[0][0:3] += start[0:3]
        result[0][3:6] += dL[0:3]
        result[0][6] = I
        for i in range(1, dense):
            result[i][0:3] += result[i-1][0:3] + dL[0:3]
            result[i][3:6] += dL[0:3]
            result[i][6] = I
        self.currentArr = cp.append(self.currentArr, result, axis=0)
        return result
    
    def getCircleCurrent(self, origin:cp.ndarray, face:cp.ndarray, radius:float, I,  dense=10):
        result = cp.zeros((dense, 7), dtype=cp.float32)

        xunit = cp.array([1, 0, 0], dtype=cp.float32)
        yunit = cp.array([0, 1, 0], dtype=cp.float32)
        zunit = cp.array([0, 0, 1], dtype=cp.float32)
        facenorm = cp.linalg.norm(face)
        faceunit = face/facenorm
        xscore = float(cp.abs(cp.dot(faceunit, xunit)))
        yscore = float(cp.abs(cp.dot(faceunit, yunit)))
        zscore = float(cp.abs(cp.dot(faceunit, zunit)))
        minscore = min(xscore, yscore, zscore)
        u1 = cp.zeros((3,1), dtype=cp.float32)
        u2 = cp.zeros((3,1), dtype=cp.float32)
        facenorm = cp.linalg.norm(face)
        if  xscore==minscore:
            u1 = cp.array([1, 0, 0], dtype=cp.float32)
        elif    yscore==minscore:
            u1 = cp.array([0, 1, 0], dtype=cp.float32)
        elif    zscore==minscore:
            u1 = cp.array([0, 0, 1], dtype=cp.float32)
        
        if  cp.dot(faceunit, u1)==0:
            u1_ = u1
        else:
            u1_ = cp.dot(faceunit, u1)*faceunit
            u1_ = u1 - u1_
            u1_ = u1_/cp.linalg.norm(u1_)
        u2_ = cp.cross(faceunit, u1_)
        u1 = u1_
        u2 = u2_    #direction of rotation is u1 to u2, same as current flow
        dtheta = 2*cp.pi/dense
        for i in range(dense):
            temp = cp.cos(dtheta*i)*u1*radius
            temp += cp.sin(dtheta*i)*u2*radius
            temp += origin
            result[i][0:3] = temp
        result[0][3:6] = result[0][0:3]-result[-1][0:3]
        result[0][6] = I
        for i in range(1, dense):
            result[i][3:6] = result[i][0:3]-result[i-1][0:3]
            result[i][6] = I
        self.currentArr = cp.append(self.currentArr, result, axis=0)
        return result