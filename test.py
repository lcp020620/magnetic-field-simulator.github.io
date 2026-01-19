import numpy as np
from functools import reduce

# 1. 데이터 생성 (내부 요소가 1인 튜플 5개)
t1 = (np.array([1, 2, 3]),)
t2 = (np.array([3, 4, 5]),)
t3 = (np.array([5, 6, 7]),)
t4 = (np.array([7, 8, 9]),)
t5 = (np.array([1, 5, 10]),)

# 2. 각 튜플에서 ndarray 추출
tuples_list = [t1, t2, t3, t4, t5] 
arrays = [t[0] for t in tuples_list]

# 3. numpy.union1d를 사용하여 중복 없이 합치기
# reduce를 사용하면 여러 배열에 대해 순차적으로 union1d를 적용합니다.
result = reduce(np.union1d, arrays)

print(result)
# 출력: [ 1  2  3  4  5  6  7  8  9 10]
