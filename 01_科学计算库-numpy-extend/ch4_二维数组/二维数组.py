#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
4.1 创建二维数组
"""

# 传List
array_1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array_1)
print(array_1.dtype)

# 传tuple 我觉得这种不好
array_2 = np.array(([1, 2, 3], [4, 5, 6]))
print(array_2)

"""
4.2 重新设置形状
"""
# 先看下二维设置为二维
array_3 = np.array([[1, 2, 3], [4, 5, 6]])
print(array_3.shape)  # (2, 3)
array_3_reshaped = array_3.reshape(3, 2)
print(array_3_reshaped)  # 不会影响原来的，需要重新搞一个去接收

# 其实一维也可以设置为二维的
array_4 = np.arange(1, 10)
print(array_4.shape)  # (9,)

array_4_reshaped = array_4.reshape(3, 3)  # 结论：只要是相乘等于原来的数字即可 3*3=9
print(array_4_reshaped)
# [[1 2 3]
#  [4 5 6]
# [7 8 9]]

"""
4.3 创建二维数组的更多方式
"""
# 创建全是1的
ones_array = np.ones(shape=(2, 3), dtype=np.int)
print(ones_array)
# [[1 1 1]
#  [1 1 1]]

# 同理还有全是0的
zero_array = np.zeros(shape=(2, 3), dtype=np.int)
print(zero_array)
# [[0 0 0]
#  [0 0 0]]


# empty 函数可以根据指定的形状和数据类型生成数组,其中的没有初始化 没有初始化，我觉得意思是这些值是瞎搞的
empty_array = np.empty(shape=(10, 3), dtype=np.int)
print(empty_array)

# full 函数可以根据指定的形状和数据类型生成数组,并用指定数组填充

# 可以直接给个2行3列的数据
full_array = np.full(shape=(2, 3), fill_value=[[1, 2, 3],
                                               [2, 3, 4]])
print(full_array)
# [[1 2 3]
#  [2 3 4]]

# 也可以给个一行的，让它去广播
full_array_2 = np.full(shape=(2, 3), fill_value=[1, 2, 3])
print(full_array_2)
# [[1 2 3]
#  [1 2 3]]

"""
4.4 数组的属性
"""

array_prop = np.array([1, 2, 3])
print(array_prop.ndim)  # 数组的维度
print(array_prop.shape)  # 数组的形状，每个维度的元素个数
print(array_prop.size)  # 数组的元素总个数
print(array_prop.itemsize)  # 每个元素的大小，以字节为单位
print(array_prop.nbytes)  # 数组总字节大小，以字节为单位。等于 size * itemsize

"""
4.5 数组的轴
"""

# 二维数组
array_np_ndim_2 = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

# 这是一个3行3列的数组，其中0轴是行，1轴是列，你可以把它理解为一个excel

# 三维数组
array_np_ndim_3 = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                            [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
                            [[30, 31, 32], [33, 34, 35], [36, 37, 38]],
                            [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])

print(array_np_ndim_3.shape)  # (4, 3, 3)
# 这是一个三维数组，这种的我们就没有二维数组好理解了，其实第一个轴0轴可以认为是样本轴，这里是4，也就是有4个二维数组，那么怎么确定它是几维数组呢，其实
# 很简单，就是看前面有个括号 ([[[ 你看这就是三维的

"""
4.6 数组的转置
"""

# 数组的 T 属性（或者transpose方法）可以转置数组，将数组轴的索引倒置
# 一维数组转置后不变，也可以认为不能转置
# 数组形状为（n, m）,转置后的形状为（m, n）
# 数组形状为（a0, a1,…,an-1,an）,转置后的形状为（an, an-1,…,a1,a0）
# 注意：转置后的是新数组不影响原来的

# 一维数组
array_t_1 = np.array([1, 2, 3])
print(array_t_1.T)  # [1 2 3]
print(array_t_1.transpose())  # [1 2 3]

# 二维数组
array_t_2 = np.array([[1, 2, 3],
                      [4, 5, 6]
                      ])

print(array_t_2)
# [[1 2 3]
#  [4 5 6]]
print(array_t_2.shape)  # (2, 3)

array_t_2_transposed = array_t_2.transpose()
print(array_t_2_transposed)
# [[1 4]
#  [2 5]
# [3 6]]
print(array_t_2_transposed.shape)  # (3, 2)

# 三维数组
array_t_3 = np.array([[[10, 11], [13, 14], [16, 17]],
                      [[20, 21], [23, 24], [26, 27]],
                      [[30, 31], [33, 34], [36, 37]],
                      [[30, 31], [33, 34], [36, 37]]])

print(array_t_3)
print(array_t_3.shape)  # (4, 3, 2)

array_t_3_transposed = array_t_3.transpose()
print(array_t_3_transposed.shape)  # (2, 3, 4)

# 看上面的结果，你懂我意思了吧， (4, 3, 2) ->  (2, 3, 4) 这难道不是形状倒序吗


"""
练习
"""
print('**练习**' * 18)
# 编写 NumPy 程序将给定数组转换为列表

a = [[1, 2], [3, 4]]
x = np.array(a)
a2 = x.tolist()
print(a == a2)  # True

# 编写一个 NumPy 程序来创建一个空数组
empty_test = np.empty(shape=(2, 3))
print(empty_test)  # 里面的值是随机的

# 编写一个 NumPy 程序来创建一个数组，并使用 full 函数填充。
full_array_test = np.full(shape=(2, 3), fill_value=[[1, 2, 3],
                                                    [2, 3, 4]])
print(full_array_test)

# 编写一个 NumPy 程序来创建一个大小为 2 x 3 的二维数组，并打印数组、数组形状和类型
array_test_23 = np.array([[2, 3, 4], [5, 6, 7]])
print(array_test_23)
print(array_test_23.shape)  # (2, 3)
print(array_test_23.dtype)  # int64
