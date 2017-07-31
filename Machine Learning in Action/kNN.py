#!/usr/bin/env python
# -*- coding: utf-8 -*-

# k邻近算法

import numpy as np
import operator

# 定义数据
def createDataSet():
	group = np.array([
		[1.0, 1.1],
		[1.0, 1.0],
		[0, 0],
		[0, 0.1]
	])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

def classify0(inx, dataSet, labels, k):
	# 取出行数
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inx, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(1)
	distances = sqDistances ** 0.5
	# 按照从小到大的顺序获取值的索引
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

if __name__ == '__main__':
	group, labels = createDataSet()

	result = classify0([1, 0], group, labels, 3)
	print(result)