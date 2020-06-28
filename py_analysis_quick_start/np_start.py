import numpy as np

# 使用 np 生成 ndarray 数据
t1 = np.array([1,2,3])

print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(10)
print(t3)
print(type(t3))
print(t3.dtype)

# np 中的数据类型
t4 = np.array(range(1, 4), dtype="float")
print(t4)
print(t4.dtype)

# 调整数据类型
t5 = t3.astype("int8")
print(t5)
print(t5.dtype)