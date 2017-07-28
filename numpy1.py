#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# # 生成矩阵
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# # 输出维度
# print(arr.ndim)

# # 输出行数和列数
# print(arr.shape)

# # 输出元素总数
# print(arr.size)

#=========================================

# 定义数据Type

# arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
# print(arr)
# print(arr.dtype)

# arr = np.linspace(1, 10, 20).reshape((4, 5))
# print(arr)

#=========================================

# a = np.array([10, 20, 30, 40])
# b = np.arange(4)

# # print(a)
# # print(b)

# # print(a * np.sin(a))

# np.dot()


# a = np.array([[1, 2], [1, -1]])
# b = np.array([[1, 2, -3], [-1, 1, 2]])
# print(a)
# print(b)
# print(np.dot(a, b))


# a = np.random.random((2, 3))
# print(a)

# # axis 0是行，1是列
# print(np.sum(a, axis=1))
# print(np.min(a))
# print(np.max(a))

# a = np.arange(14, 2, -1).reshape(3, 4)

# print(a)

# # print(np.transpose(a))
# # print(a.T)

# b = np.clip(a, 5, 8)

# print(b)
# print(np.argmin(b, axis=1))


# a = np.arange(3, 15).reshape(3, 4)
# print(a)
# # print(a.flatten())
# for row in a.flat:
# 	print(row)

# a = np.array([1, 1, 1])
# b = np.array([2, 2, 2])

# print(a.T)

# a = np.arange(12).reshape(3, 4)
# print(np.array_split(a, 3, axis=1))

# a = np.arange(4)
# b = a.copy()

# s = pd.Series([1, 3, 6, np.nan, 44, 1])
# print(s)

dates = pd.date_range('20170101', periods = 6)
# print(dates)

# df = pd.DataFrame(np.random.random((6, 4)), index=dates, columns=['a', 'b', 'c', 'd'])
# print(df)

# df = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(df)

df = pd.DataFrame({'A': 1, 'b': 2, 'c': [1, 2, 3]})
print(df)
print('===================')
print(df[df.c > 1])