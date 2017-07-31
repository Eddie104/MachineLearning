#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Numpt拥有以下集中属性:
# ndim：维度
# shape：行数和列数
# size：元素个数
def array_to_matrix(array):
	array = np.array(array)
	print(array)
	print('维度 => %d' % array.ndim)
	print('形状: =>')
	print(array.shape)
	print('元素个数 => %d' % array.size)

def create_by_array(array):
	return np.array(array)

# 指定数据 dtype
# dtype取值有np.int64 np.int32 np.float32 np.float64 等等
def create_by_dtype(array, dtype):
	return np.array(array, dtype=dtype);

# 创建全零数组
def create_by_zeros(size, dtype=None):
	return np.zeros(size, dtype=dtype)

# 创建全一数组
def create_by_ones(size, dtype=None):
	return np.ones(size, dtype=dtype)

# 创建全空数组, 其实每个值都是接近于零的数
def create_by_empty(size):
	return np.empty(size)

if __name__ == '__main__':
	# array_to_matrix([[1,2,3], [4,5,6]])
	# a = create_by_array([1,2,3])
	# a = create_by_dtype([1,2,3], np.float)
	# a = create_by_zeros((3,4), np.int32)
	# a = create_by_ones((3,4), np.int32)
	# a = create_by_empty((3,4))
	# 用 arange 创建连续数组:
	# a = np.arange(0, 11, 1)
	# a = np.arange(12)
	# 使用 reshape 改变数据的形状
	# a = np.arange(12).reshape((3, 4))
	# 用 linspace 创建线段型数据:
	# 开始端1，结束端10，且分割成20个数据，生成线段
	# a = np.linspace(1, 10, 20)
	
	# numpy的运算
	# a = np.array([10, 20, 30, 40])
	# b = np.arange(4)
	# # c = a + b
	# # c = a * b
	# c = b ** 3
	# print(a)
	# print(b)
	# print(c)
	# print(b < 2)
	# print(b == 2)
	# 二维矩阵的运算
	# a = np.arange(4).reshape((2, 2))
	# b = np.arange(3, 7).reshape((2, 2))
	# print(a)
	# print(b)
	# c = a * b
	# d = a.dot(b)
	# print(c)
	# print(d)
	
	# a = np.random.random((2, 4))
	# print(a)
	# print(a.sum())
	# print(a.min())
	# print(a.max())
	
	# a = np.random.random((2, 3))
	# print(a)
	# print(a.sum(1))
	# print(a.sum(0))
	
	# a = np.random.random((3, 4))
	# print(a)
	# # 最小值的索引
	# print(a.argmin())
	# # 最大值的索引
	# print(a.argmax())
	# # 求平均值
	# print(np.average(a))
	# print(a.mean())
	# # 求中位数
	# print(np.median(a))

	# print(a.cumsum())
	# print(np.diff(a))

	# print(np.nonzero(a))

	# print(np.sort(a))
	# 
	
	a = np.arange(12).reshape((3, 4))
	print(a)
	b = a.transpose()
	print(b)