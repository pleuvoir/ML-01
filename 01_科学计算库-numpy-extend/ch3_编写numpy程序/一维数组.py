#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
3.1 创建一维数组
"""

# 传list
array = np.array([1, 2, 3])
print(array.shape)  # (3,)

# 传tuple都可以
np_array_2 = np.array((1, 2, 3))
print(np_array_2.shape)  # (3,)

# 可以使用随机函数 类似range
np_array_arange = np.arange(1, 5, 1, dtype=np.int32)
print(np_array_arange)  # [1 2 3 4]

# 也可以做等差数列 ，注意这个 5 不是步长而是指生成几个数
np_array_arange_linspace = np.linspace(0, 100, 5, endpoint=True, dtype=np.int32)
print(np_array_arange_linspace)  # [  0  25  50  75 100]

# 还可以做等比数列（这里数字不要乱传）  起点 2的0次方，终点2的9次方，生成10个数字
np_array_arange_logspace = np.logspace(0, 9, 10, base=2.0, endpoint=True, dtype=np.float)
print(np_array_arange_logspace)  # [  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]

"""
3.2 数据类型
"""
np_array_3 = np.array([1, 2, 3])
print(np_array_3.dtype)  # int64

np_array_4 = np.array([1., 2, 3])
print(np_array_4.dtype)  # float64

# 可以在创建时直接指定类型
np_array_5 = np.array([1, 2, 3], dtype=float)
print(np_array_5)  # [1. 2. 3.]
print(np_array_5.dtype)  # float64

np_array_6 = np.array([1 + 2j, 3 + 4j, 5 + 6j])
print(np_array_6)  # [1.+2.j 3.+4.j 5.+6.j]
print(np_array_6.dtype)  # complex128 复数类型，说实话我还不知道这有什么用

np_array_7 = np.array([True, False, False])
print(np_array_7)  # [ True False False]
print(np_array_7.dtype)  # bool

np_array_8 = np.array(['你好', 'hello', 'world'])
print(np_array_8)  # ['你好' 'hello' 'world']
print(np_array_8.dtype)  # <U5

# 转换类型
np_array_9 = np.array([1, 2, 3])
np_array_10 = np_array_9.astype(np.float)  # 会创建一个新对象

"""
练习
"""

print('**练习**' * 18)
# 编写一个 NumPy 程序来创建一个从 30 到 50 的所有偶数整数的数组， 取值[30, 50)

array_prac_1 = np.arange(30, 50)
array_prac_2 = array_prac_1[array_prac_1 % 2 == 0]
print(array_prac_2)  # [31 33 35 37 39 41 43 45 47 49]

print(np.arange(30, 50, 2))  # 这样也行

# 编写 NumPy 程序以获取有关 np.add 函数的帮助信息
# print(np.info(np.add))

# 编写 NumPy 程序创建介于 2.5 到 6.5 之间 30 个均匀间隔元素的一维数组，包括 6.5
linspace_array = np.linspace(2.5, 6.5, 30)
print(linspace_array)

# 编写 NumPy 程序创建 20 元素的等比数列数组，指数介于 2 到 5，包括5
print(np.logspace(2,5,20))