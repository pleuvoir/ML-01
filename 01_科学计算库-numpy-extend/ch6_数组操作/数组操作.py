import numpy as np

"""
6.1 连接数组  
（我觉得会用concatenate就行）
"""

# 使用 concatenate 函数

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
ab = np.concatenate((a, b))
print(ab)
# [[1 2]
#  [3 4]
# [5 6]]

zero_array = np.zeros(shape=(2, 3), dtype=np.int)
ones_array = np.ones(shape=(1, 3), dtype=np.int)
concatenated_array = np.concatenate((zero_array, ones_array))
print(concatenated_array)
# [[0 0 0]
#  [0 0 0]
# [1 1 1]]

# 默认是按样本轴进行连接的
a_1 = np.array([[1, 2], [3, 4]])
b_1 = np.array([[5, 6]])
aba = np.concatenate((a_1, b_1), axis=0)
print(aba)
# [[0 0 0]
#  [0 0 0]
# [1 1 1]]

# 换个轴试试  a_1 shape (2,2) b_1 shape(1,2) 需要把b_1进行转置 (2,1) 然后拼1轴
abac = np.concatenate((a_1, b_1.T), axis=1)
print(abac)
# [[1 2 5]
#  [3 4 6]]

# 使用 hstack 函数
# hstack函数沿水平堆叠多个数组，相当于concatenate函数axis=1情况

zeros_h = np.zeros(shape=(2, 3), dtype=np.int)
one_h = np.ones(shape=(2, 1), dtype=np.int)

hstackd_array = np.hstack((zeros_h, one_h))
print(hstackd_array)
# [[0 0 0 1]
#  [0 0 0 1]]

# 使用 vstack 函数
# vstack函数沿垂直堆叠多个数组，相当于concatenate函数axis=0情况
ones_v = np.ones(shape=(2, 3))
zeros_v = np.zeros(shape=(4, 3))

vstackd_array = np.vstack((ones_v, zeros_v))
print(vstackd_array)
# [[1. 1. 1.]
#  [1. 1. 1.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]
# [0. 0. 0.]]

"""
6.2 分割数组
"""

# 使用 split 函数

# 一维的情况
arange_array = np.arange(9)
split = np.split(arange_array, 3)  # 如果是数字就平均分
print(split)  # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]

np_split = np.split(arange_array, [2, 5, 7])  # 分为几个左包右不包区间
print(np_split)  # array([0, 1]), array([2, 3, 4]), array([5, 6]), array([7, 8])]

# 二维的情况
reshaped = arange_array.reshape(3, 3)
print(reshaped)
# [[0 1 2]
#  [3 4 5]
# [6 7 8]]
lx = np.split(reshaped, 3, axis=0)  # 默认按0轴切分
print(lx)  # [array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]

ly = np.split(reshaped, 3, axis=1)  # 按y轴切分
print(ly)
# [array([[0],
#         [3],
#         [6]]),
#  array([[1],
#          [4],
#         [7]]),
#  array([[2],
#         [5],
#         [8]])]

# 按数组切分下试试
new_array = np.arange(12).reshape(4, 3)
print(new_array)
# [[ 0  1  2]
#  [ 3  4  5]
# [ 6  7  8]
# [ 9 10 11]]

lt = np.split(new_array, [1, 3], axis=0)  # [0,1) [1,3) [3,..
print(lt)
# [array([[0, 1, 2]]),
#  array([[3, 4, 5],[6, 7, 8]]),
#  array([[ 9, 10, 11]])]

# 使用 hsplit 函数 沿水平方向分割数组，相当于 split 函数 axis=1 情况

# 使用 vsplit 函数 沿垂直方向分割数组，相当于 split 函数 axis=0 情况


"""
6.3 算数运算
"""

# 这个其实就是逐元素运算
reshaped_opt = np.arange(6).reshape(3, 2)
print(reshaped_opt)
# [[1 2]
#  [3 4]
# [5 6]]

print(reshaped_opt + 1)
print(reshaped_opt - 1)
print(reshaped_opt * 3)
print(reshaped_opt / 10)

"""
6.4 广播
不同的形状数组或标量计算时发生广播。
"""

# 标量广播
base = np.arange(10)
print(base * 10)  # [ 0 10 20 30 40 50 60 70 80 90]

# 数组广播
# 广播规则：
# 1、如果两个数组维度不相等，维度较低的数组的形状（shape）会从左则开始填充 1，直到维度与高维数组相等。
# 2、如果两个数组维度相等时，要么对应轴的长度相同，要么其中一个长度为 1，则是兼容数组可以广播。长度为 1 的轴会被扩展。

# 简而言之就是 (4,3) 的可以和 (3,)的计算

x_base = np.arange(12).reshape(4, 3)
print('x_base：', x_base, sep='\n')
# [[ 0  1  2]
#  [ 3  4  5]
# [ 6  7  8]
# [ 9 10 11]]

y_base = np.arange(3).reshape(3, )
print('y_base：', y_base, sep='\n')
# [[0 1 2]

# y_base 会按照广播规则1 变为 (1,3) 然后重复4行
print(x_base + y_base)
# [[ 0  2  4]
#  [ 3  5  7]
# [ 6  8 10]
# [ 9 11 13]]
