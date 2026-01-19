import cupy as cp
import time

num = 5000
v1 = cp.random.randn(num*2, 3)
v2 = cp.random.randn(num, 3)
v1_exp = v1[:, cp.newaxis, :]
v2_exp = v2[cp.newaxis, :, :]
start = time.time()
result = cp.cross(v1_exp, v2_exp) #벡터 외적 구할려면 차라리 3차원 ndarray끼리의 외적으로 구현하는 게 더 빠름
end = time.time()
print(f"{end-start:.5f} sec")


# 예: 1,000,000개의 3차원 벡터 쌍 생성
n = 5
v1 = cp.random.randn(n, 3)
v2 = cp.random.randn(n, 3)

# 모든 벡터 쌍에 대해 동시에 외적 계산 (GPU 병렬 처리)
# axis=-1이 기본값이므로 자동으로 각 행(3성분)끼리 연산함
result = cp.cross(v1, v2)
normv1 = cp.linalg.norm(v1, axis=1, keepdims=True) #이렇게 안하면 전체 숫자에 대한 norm을 구함
print(normv1)
print('-----------')
unitv1 = v1/normv1
print(unitv1)
print('-----------')
print(unitv1/normv1)
print('===========')

# 1. Create vectors directly on the GPU
vector_gpu_a = cp.array([1, 2, 3], dtype=cp.float32)
vector_gpu_b = cp.array([4, 5, 6], dtype=cp.float32)

# 2. Element-wise operations (addition, subtraction, multiplication)
# These operate just like NumPy
sum_vec = vector_gpu_a + vector_gpu_b
diff_vec = vector_gpu_a - vector_gpu_b
prod_vec = vector_gpu_a * vector_gpu_b  # Element-wise multiplication

# 3. Dot product
# Use cp.dot() or cp.inner()
dot_product = cp.dot(vector_gpu_a, vector_gpu_b)

# 4. Cross product
# Use cp.cross()
try:
    cross_product = cp.cross(vector_gpu_a, vector_gpu_b)
except ValueError as e:
    # Cross product generally needs 3D vectors
    pass 

# 5. L2 Norm (Magnitude)
# Use cp.linalg.norm()
magnitude_a = cp.linalg.norm(vector_gpu_a)

# 6. Convert the result back to NumPy on the CPU
# Use cp.asnumpy() to retrieve the data from the GPU
dot_product_cpu = cp.asnumpy(dot_product)

print(f"GPU Vector A: {vector_gpu_a}")
print(f"GPU Vector B: {vector_gpu_b}")
print(f"Element-wise sum: {sum_vec}")
print(f"Dot product (on CPU after transfer): {dot_product_cpu}")