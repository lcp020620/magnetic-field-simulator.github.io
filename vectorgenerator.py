import cupy as cp

def row(a, b, c):
    return cp.array([a, b, c], dtype=cp.float32)
zeroVec = row(0, 0, 0)

class VectorGenerator:
    def __init__(self):
        self.vecArray = cp.zeros((0, 3), dtype=cp.float32)
    
    def line(self, start:cp.ndarray=zeroVec, end:cp.ndarray=zeroVec, dense:int=10):
        #start, end must be a single row vector
        result = cp.zeros((dense, 6), dtype=cp.float32)
        L = end - start
        dL = L/dense
        result[0][0:3] += start[0:3]
        result[0][3:6] += dL[0:3]
        for i in range(1, dense):
            result[i][0:3] += result[i-1][0:3] + dL[0:3]
            result[i][3:6] += dL[0:3]
        self.vecArray = cp.append(self.vecArray, result[:, 0:3], axis=0)
        return result
    
    def circle(self, origin:cp.ndarray, face:cp.ndarray=zeroVec, radius:float=1, dense:int=10):
        #start, end must be a single row vector
        result = cp.zeros((dense, 6), dtype=cp.float32)
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
        for i in range(1, dense):
            result[i][3:6] = result[i][0:3]-result[i-1][0:3]
        self.vecArray = cp.append(self.vecArray, result[:, 0:3], axis=0)
        return result
    
    def funcLine(self, fun, tstart, tend, dense):
        #function example
        # def newfun(t):
        #     return cp.transpose(cp.array([t, t*-1, t**2], dtype=cp.float32))

        t = cp.linspace(tstart, tend, dense)
        result = fun(t)
        self.vecArray = cp.append(self.vecArray, result, axis=0)
        return result