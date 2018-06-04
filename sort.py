#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhuguangpeng'
__mtime__ = '18-5-26'
"""
import math

def bubble_sort(lists):
	count = len(lists)
	for i in range(0, count):
		for j in range(i + 1, count):
			if lists[i] > lists[j]:
				lists[i], lists[j] = lists[j], lists[i]
	return lists

def select_sort(lists):
	count = len(lists)
	for i in range(0, count):
		min = i
		for j in range(i + 1, count):
			if lists[min] > lists[j]:
				min = j
		lists[min], lists[i] = lists[i], lists[min]
	return lists

def insert_sort(lst):
	n = len(lst)
	if n == 1:
		return lst
	for i in range(1, n):
		for j in range(i, 0, -1):
			if lst[j] < lst[j-1]:
				lst[j], lst[j-1] = lst[j-1], lst[j]
			else:
				break
			print(lst)
	return lst


def shell_sort(list):
	n = len(list)
	gap = n // 2
	while gap > 0:
		for i in range(gap, n):
			temp = list[i]
			j = i
			while j >= gap and list[j - gap] > temp:
				list[j] = list[j - gap]
				j -= gap
			list[j] = temp
		gap = gap // 2
	return list


def quick_sort(lists, left, right):
	if left >= right:
		return lists
	key = lists[left]
	low = left
	high = right
	print(key)
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
			print('while1')
		lists[left] = lists[right]
		print(lists)
		while left < right and lists[left] <= key:
			left += 1
			print('while2')
		lists[right] = lists[left]
		print(lists)
	print('end')
	lists[right] = key
	print(lists)
	quick_sort(lists, low, left - 1)
	quick_sort(lists, left + 1, high)
	return lists

def count_sort(list):
	min = 999999
	max = 0
	for x in list:
		if x < min:
			min = x
		if x > max:
			max = x
	count = [0] * (max - min + 1)
	for index in list:
		count[index - min] += 1
	index = 0
	for a in range(max - min + 1):
		for c in range(count[a]):
			list[index] = a + min
			index += 1
	return list

def heap_sort(lst):
	def sift_down(start, end):
		"""最大堆调整"""
		root = start
		while True:
			child = 2 * root + 1
			if child > end:
				break
			if child + 1 <= end and lst[child] < lst[child + 1]:
				child += 1
			if lst[root] < lst[child]:
				lst[root], lst[child] = lst[child], lst[root]
				root = child
			else:
				break

	# 创建最大堆
	for start in range((len(lst) - 2) // 2, -1, -1):
		sift_down(start, len(lst) - 1)

	# 堆排序
	for end in range(len(lst) - 1, 0, -1):
		lst[0], lst[end] = lst[end], lst[0]
		sift_down(0, end - 1)
	return lst

def merge_sort(lst):
	if len(lst) <= 1:
		return lst

	def merge(left, right):
		i, j = 0, 0
		result = []
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result += left[i:]
		result += right[j:]
		return result

	middle = int(len(lst) // 2)
	left = merge_sort(lst[:middle])
	right = merge_sort(lst[middle:])
	return merge(left, right)


def radix_sort(lists, radix=10):
	K = int(math.ceil(math.log(max(lists) + 1, radix)))  
	for i in range(1, K + 1):  
		bucket = [[] for i in range(radix)]  
		for val in lists:
			bucket[val % (radix ** i) // (radix ** (i - 1))].append(val)  
		del lists[:]
		for each in bucket:
			lists.extend(each)  
	return lists

def main():
	lst = [4,8,7,9,6,5,1,2,3]
	list.sort(lst)
	print(lst)

if __name__ == "__main__":
	main()
