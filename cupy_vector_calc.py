import cupy as cp
import numpy as np

n = 10
v1 = cp.random.randn(n, 3)
v2 = cp.array([1, 0, 0], dtype=cp.float32)

m = v2.shape
print(len(m))
result = cp.cross(v1, v2)
print(type(v1))
print(v1)
print(result)