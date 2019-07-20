import random
import struct
import time
import math
from statistics import median

# Method to collect name of file to open
def collect_input():
	user_input = input('Enter name of file to open: ')
	return user_input

# Method to open bin file and read contents
def read_bin(file_name):
	original = []
	with open(file_name, 'rb') as file:
		data = file.read()
		size = struct.unpack('i', data[0:4])
		for i in range(4, size[0]+4):
			element = struct.unpack('i', data[i:i+4])
			original.append(element[0])
		print(original)
		return original

# Method to create binary file
def create_bin():

	NUM_INTEGERS = 4

	with open('file.bin', 'wb') as file:

		file.write(struct.pack('i', NUM_INTEGERS))

		for i in range(NUM_INTEGERS):
			file.write(struct.pack('i', random.randint(0, 1000000000)))

# Method to check if array is in non-decreasing order
def is_ordered(array):
	for i in range(1, len(array)):
		if array[i-1] > array[i]:
			return False
	return True

# Insertion Sort method
def insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		j = i-1

		while j >= 0 and key < array[j]:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = key
	return array

# Quick Sort method
def quick_sort(array, start, end):
	if len(array) < 5:
		insertion_sort(array)
		return array
	pivot_index = median3(array)
	pivot_index = partition(array, start, end, pivot_index)
	# quick_sort(array, start, pivot_index+1)
	# quick_sort(array, pivot_index-1, end)


# Method to find median3 of array
def median3(array):
	if len(array) < 3:
		return median(array)
	median_list = []
	center = math.floor(len(array)/2)
	# Get first/last/center element from array
	median_list.append(array[0])
	median_list.append(array[-1])
	median_list.append(array[center])
	print(f'The median list is: {median_list}')
	print(f'The pivot is: {median(median_list)}')
	median_value = median(median_list)
	return array.index(median_value)

# def median3(array):
# 	a = array[0]
# 	b = math.floor(len(array)/2)
# 	c = array[-1]

# 	if a <= b <= c or c <= b <= a:
# 		return array.index(b)
# 	elif b <= a <= c or c <= a <= b:
# 		return array.index(a)
# 	else:
# 		return array.index(c)


# Method to partition list
def partition(array, left, right, pivotIndex):
	pivot_value = array[pivotIndex]
	swap(array, pivotIndex, right)

	store = left
	for i in range(left, right+1):
		if array[i] <= pivot_value:
			swap(array, store, i)
			store += 1
	swap(array, right, store)
	print(f'The array is now: {array}')
	return store

# Method to swap elements in list
def swap(array, pos1, pos2):
	array[pos1], array[pos2] = array[pos2], array[pos1]
	return array

# ------------
# Buffer VM
# ------------
def buffer_insertion():
	array_sorted = read_bin('sorted.bin')
	for i in range(5):
		insertion_sort(array_sorted)

	array_random = read_bin('random.bin')
	for i in range(5):
		insertion_sort(array_random)

	array_reverse = read_bin('reverse.bin')
	for i in range(5):
		insertion_sort(array_reverse)

def buffer_quick():
	array_sorted = read_bin('sorted.bin')
	for i in range(5):
		quick_sort(array_sorted)

	array_random = read_bin('random.bin')
	for i in range(5):
		quick_sort(array_random)

	array_reverse = read_bin('reverse.bin')
	for i in range(5):
		quick_sort(array_reverse)

# ------------
# Tester
# ------------
def test_main():
	# partition_list = [-81, 22, 45, 27, 34, 98, 67]
	# print(f'The partition list is: {partition_list}')
	# pivot_index = median3(partition_list)
	# print(f'The pivot index is : {pivot_index}')
	# store = partition(partition_list, 0, len(partition_list)-1, pivot_index)

	# Quick Sort
	quick_list_1 = [-21, 22, 48, 74, 92, 7, 28, 19, -21, 29, 39, 44, 76, 46]
	quick_list_2 = [5, 3, 2, 1]
	sorted_array = quick_sort(quick_list_1, 0, len(quick_list_1) -1)
	# sorted_array = quick_sort(quick_list_2, 0, len(quick_list_2)-1)
	print(sorted_array)

# ------------
# Test
# ------------
def main():
	# Collect file_name to be read
	file_name = collect_input()
	original_1 = read_bin(file_name)
	print(f'Array Ordered: {is_ordered(original_1)}')

	# Time insertion sort
	time_1 = time.clock()
	original_1 = insertion_sort(original_1)
	elapsed_time = time.clock() - time_1
	print(f'Array Ordered: {is_ordered(original_1)}, Time Taken: {format(elapsed_time, ".2e")}')
	print(original_1)


if __name__ == '__main__':
	test_main()

