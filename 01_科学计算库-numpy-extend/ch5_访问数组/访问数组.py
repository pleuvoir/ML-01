#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
5.1 索引访问
"""

# 一维数组
array_1 = np.array([1, 2, 3, 4, 5, 6])
print(array_1[0])  # 1
print(array_1[-2])  # 5

# 二维数组
array_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2[1])  # [4 5 6]
print(array_2[1][2])  # 6
print(array_2[1, 2])  # 6 这个和上面的是等价的，我觉得上面的形式更好理解一些，奈何大家都用这种

"""
5.2 切片访问
"""

# 一维数组切片访问和python是一样的
array_slice = np.array([1, 2, 3, 4, 5, 6, 7])
print(array_slice[1:3])  # [2 3]
print(array_slice[::2])  # [1 3 5 7]
print(array_slice[::3])  # [1 4 7]

# 二维数组切片访问 np.array[所在 0 轴切片, 所在 1 轴切片,..., 所在 n-1 轴切片]
# 注意：这块就和索引访问不同了，只有这一种形式，不要使用 [][][]这种去访问！
array_slice_2 = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
print(array_slice_2[::-1, :2])  # 我觉得这个只要理解了就没问题了
# [[7 8]
#  [4 5]
# [1 2]]


"""
5.3 布尔索引
"""

# 一维数组使用布尔索引，只取True对应位置的数据
array_bool = np.array([1, 2, 3, 4, 5, 6])
array_bool_index = np.array([False, True, False, True, False, True])
print(array_bool[array_bool_index])  # [2 4 6]

# 二维数组使用布尔索引

array_bool_2 = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

array_bool_2_index = np.array([[False, False, True],
                               [False, True, False],
                               [False, True, False]])
print(array_bool_2[array_bool_2_index])  # [3 5 8]

# 注意：
# 布尔数组必须与要索引的数组形状相同，否则引发IndexError错误
# 布尔索引返回的新数组是原数组的副本，与原数组不共享相同的数据空间。新数组的修改不会影响原数组。这是所谓的深克隆

"""
5.4 花式索引
"""

# 一维数组花式索引 原始数组是一维数组,索引数组可以是一维或多维的
array_hua = np.array([1, 2, 3, 4, 5, 6])
print(array_hua[np.array([0, 2, 3])])  # [1 3 4]
print(array_hua[[0, 2, 3]])  # 其实也可以直接用列表去访问，不必做个ndarray

# 索引数组是多维，那么获得的结果就和索引的shape一样，将对应位置的值填进去罢了
array_index_muti = np.array([[1, 2], [4, 5], [1, 1]])
print(array_index_muti.shape)  # (3,2)
print(array_hua[array_index_muti])
# [[2 3]
#  [5 6]
# [2 2]]

# 二维数组花式索引 原始数组是多维数组,索引数组可以是一维或多维的
arange_array = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
arange_array_reshaped = arange_array.reshape(2, 5)
print(arange_array_reshaped)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

# 这种是一维索引
array_index_0 = np.array([0, 0, 1])  # 这个其实就是0轴索引
array_index_1 = np.array([0, 1, 3])  # 这个其实就是1轴索引
# 上面的两个结合起来就构成了 (x,y) (0,0) (0,1) (1,3) 最后出来的就是3个数
print(arange_array_reshaped[array_index_0, array_index_1])
# [0 1 8]

# 这种是二维索引
array_index2_0 = np.array([[1, 1],
                           [1, 0]])
array_index2_1 = np.array([[1, 0],
                           [3, 2]])
# 同理，上面的逐元素结合起来就是 一个新的(2,2)索引坐标数组
print(arange_array_reshaped[array_index2_0, array_index2_1])
# [[6 5]
#  [8 2]]

# 上面的情况都是构建列表，其实可以把列表和整数混合使用，比如0轴索引还是用上面的，1轴来个整数3，其实就相当于1轴的是 (2,2)形状值全是3
print(arange_array_reshaped[array_index2_0, 3])
# [[8 8]
#  [8 3]]


"""
5.5 迭代数组
"""

a = np.arange(0, 12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
# [ 8  9 10 11]]

print('迭代输出元素：')
for n in np.nditer(a):
    print(n, end="|")
# 0|1|2|3|4|5|6|7|8|9|10|11|

"""
练习
"""
print('**练习**' * 18)

# 编写一个 NumPy 程序来创建一个 10x10 矩阵，其中边界上的元素是 1， 内部元素是 0

ones_array = np.ones(shape=(10, 10), dtype=np.int)
print(ones_array)
ones_array[1:-1, 1:-1] = 0
print(ones_array)
