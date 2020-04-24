#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
7.1 数学运算函数
"""

# 算数运算函数（这个和ch6_数组操作中的一样，因为那章需要讲广播，所以带了一下）
print('算数运算函数')
array_1 = np.array([[1, 2, 3],
                    [4, 5, 6]])
array_2 = np.arange(0, 3)

print('+')
print(array_1 + array_2)
print(np.add(array_1, array_2))
# [[1 3 5]
#  [4 6 8]]

print('-')
print(array_1 - array_2)
print(np.subtract(array_1, array_2))
# [[1 1 1]
#  [4 4 4]]

print('*')
print(array_1 * array_2)
print(np.multiply(array_1, array_2))
# [[ 0  2  6]
#  [ 0  5 12]]

print('/')
print(array_1 / array_2)
print(np.divide(array_1, array_2))
# [[inf 2.  1.5]  0不能被除，它会抛出异常，但是继续执行下去 RuntimeWarning: divide by zero encountered in true_divide
#  [inf 5.  3. ]]

# 关系运算函数（数组之间做比较，得出布尔值）
print('关系运算函数')
array_3 = np.arange(12).reshape(4, 3)
print(array_3)
# [[ 0  1  2]
#  [ 3  4  5]
# [ 6  7  8]
# [ 9 10 11]]
array_4 = np.arange(1, 4)
print(array_4)
# [1 2 3]
print('<')
print(array_3 < array_4)  # 会广播低纬度的
# [[ True  True  True]
#  [False False False]
# [False False False]
# [False False False]]

print('==')
print(array_3 == array_4)
print(np.equal(array_3, array_4))  # 都是一样的，需要时候再查吧

"""
7.2 自定义通用函数
用户自定义一个函数，进行逐元素运算
"""

print('自定义通用函数')


def abs_more(x, y):
    return abs(x + y), abs(x - y)


# 传入数组参数个数2，返回2个数组
new_func = np.frompyfunc(abs_more, 2, 2)

array_5 = np.arange(-12, 0).reshape(4, 3)
print(array_5)
# [[-12 -11 -10]
#  [ -9  -8  -7]
#  [ -6  -5  -4]
#  [ -3  -2  -1]]

array_6 = np.arange(3)
print(array_6)  # [0 1 2]

add, substract = new_func(array_5, array_6)
print('add')
print(add)
# [[12 10 8]
#  [9 7 5]
# [6 4 2]
# [3 1 1]]

print('substract')
print(substract)
# [[12 12 12]
#  [9 9 9]
# [6 6 6]
# [3 3 3]]

"""
8.1 随机数
"""

# 常用随机数

print('常用随机数')
random_array = np.random.random(10)  # 生成10个 0-1之间的数
print(random_array)
# [0.40067346 0.99690032 0.2148416  0.6733348  0.87010673 0.43761419
#  0.48943912 0.78511117 0.61777445 0.58047221]

randint = np.random.randint(1, 3, dtype=np.int, size=(3, 2))  # [1,3)  指定shape
print(randint)
# [[1 2]
#  [2 2]
# [1 1]]

print('正态分布随机数')
