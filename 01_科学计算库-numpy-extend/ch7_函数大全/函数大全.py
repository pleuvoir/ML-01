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
# print(array_1 / array_2)
# print(np.divide(array_1, array_2))
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


rand_array_2 = np.random.rand(10)  # 和上面的一样
print(rand_array_2)
# [0.07948068 0.20362212 0.98910528 0.65472643 0.66455877 0.51172147
#  0.81954455 0.77833053 0.68400935 0.21733152]

randint = np.random.randint(1, 3, dtype=np.int, size=(3, 2))  # [1,3)  指定shape int类型的
print(randint)
# [[1 2]
#  [2 2]
# [1 1]]

print('正态分布随机数')

# 标准的正态分布，以0位平均数
randn_array = np.random.randn(5)
print(randn_array)
# [-2.33418873  0.46356454 -2.26480846  1.01616359 -1.94167289]

randn_2 = np.random.randn(3, 2)
print(randn_2)
# [[ 1.65977431  0.16289338]
#  [ 0.12188722 -0.83643825]
#  [-0.48954999 -1.04473608]]

# 以10010为平均值，标准差为100，生成6个
normal = np.random.normal(10010, 100, 6)
print(normal)
# [10113.26620434 10144.56822252 10148.8080794  10094.82888583
#  10106.74567212 10053.16515397]


random_normal_2 = np.random.normal(0, 10, (3, 2))  # 把第一个参数设为0就是标准正态分布
print(random_normal_2)
# [[-1.23015849 -0.72917127]
#  [ 5.37678415 15.56051275]
# [ 3.78467223 -0.51157825]]

"""
8.2 排序
"""

print('8.2 排序')

# 按照轴进行排序 语法 numpy.sort(a, axis=-1, kind='quicksort', order=None)

a = np.random.randint(0, 10, size=(3, 4))
print(a)
# [[2 8 4 1]
#  [6 6 2 6]
# [5 7 4 3]]
sort_a = np.sort(a, axis=1, kind='quicksort', order=None)  # 数字没字段
print(sort_a)
# [[1 2 4 8]
#  [2 6 6 6]
# [3 4 5 7]]

# 轴排序索引，返回排序后的索引（这个索引是原来位置的索引）
cidx = np.argsort(a, axis=1)
print(cidx)
# [[2 0 1 1]
#  [1 2 2 2]
# [0 1 0 0]]

"""
8.3 聚合函数
"""

print('聚合函数')

# 求和
a_sum = np.array([[5, 6],
                  [7, 8]])

np_sum_a = np.sum(a_sum)
print(np_sum_a)  # 26

np_sum_0 = np.sum(a_sum, axis=0)
print(np_sum_0)  # [12 14]

# 求最大值
max_array = np.random.randint(0, 10, size=(3, 4))
print(max_array)
# [[3 7 6 3]
#  [7 2 3 4]
# [9 1 3 7]]
print(max_array.max(axis=0))  # [9 7 6 7]

b_nan = np.array([[5, 6],
                  [7, np.nan]])

print(np.nanmax(b_nan, 0))  # [7. 6.] 忽略nan
print(np.max(b_nan, 0))  # [ 7. nan]

# 求最小值 和上面的一样 .min .nanmin

# 平均值 mean nanmean
mean = max_array.mean(axis=0)
print(mean)

# 加权平均值 numpy.average(a, axis=None, weights=None)
print('加权平均值')
av_array = np.array([[5, 6],
                     [7, 8]])
average = np.average(av_array, axis=-1, weights=[0.2, 0.8])
print(average)  # [5.8 7.8]

# unique 去重
L = [x for x in 'Hello']
array_L = np.array(L)
print(array_L)  # ['H' 'e' 'l' 'l' 'o']

unique = np.unique(array_L)
print(unique)  # ['H' 'e' 'l' 'o']

# where 其实就是三目运算符

a = np.arange(5)
print(a)
b = np.where(a < 3, a, a + 100)
print(b)  # [  0   1   2 103 104]


"""
9 数组保存
"""

# 保存
a = np.arange(9).reshape(3, 3)
np.save('arry_save1', a)


b = np.arange(10)
np.savez('arry_savez1', arry_a=a, arry_b=b) #压缩包

np.savez_compressed('arry_savez_compressed1', arry_a=a, arry_b=b)

# 读取

a1 = np.load('arry_save1.npy')
print(type(a1)) # ndarray
data1 = np.load('arry_savez1.npz')
print(type(data1),type(data1['arry_a'])) #NpzFile ndarray
data2 = np.load('arry_savez_compressed1.npz')
print(type(data2),type(data2['arry_b'])) #NpzFile
