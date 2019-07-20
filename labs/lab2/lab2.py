import random
import struct
import time

# Method to collect name of file to open
def collect_input():
	user_input = input('Enter name of file to open: ')
	return user_input

# Method to read binary file
def read_bin(file_name):
	original = []
	with open(file_name, 'rb') as file:
		data = file.read()
		size = struct.unpack('i', data[0:4])[0]
		for i in range(4, size*4+4, 4):
			element = struct.unpack('i', data[i:i+4])
			original.append(element[0])
		return original


# Methods to create binary files
def create_random_bin():
	NUM_INTEGERS = 100000
	with open('random.bin', 'wb') as file:

		file.write(struct.pack('i', NUM_INTEGERS))

		for i in range(NUM_INTEGERS+1):
			file.write(struct.pack('i', random.randint(0, 1000000000)))

def create_sorted_bin():
	NUM_INTEGERS = 100000
	with open('sorted.bin', 'wb') as file:

		file.write(struct.pack('i', NUM_INTEGERS))

		for i in range(1, NUM_INTEGERS+1):
			file.write(struct.pack('i', i))

def create_reverse_bin():
	NUM_INTEGERS = 100000
	with open('reverse.bin', 'wb') as file:

		file.write(struct.pack('i', NUM_INTEGERS))

		for i in reversed(range(1, NUM_INTEGERS+1)):
			file.write(struct.pack('i', i))


# Method to check if array is in non-decreasing order
def is_ordered(array):
	for i in range(1, len(array)):
		if array[i-1] > array[i]:
			return False
	return True

# Method to find the median of three
def median3(array, left, right):
    mid = (left+right-1)//2
    a = array[left]
    b = array[mid]
    c = array[right-1]
    if a <= b <= c:
        return mid
    if c <= b <= a:
        return mid
    if a <= c <= b:
        return right-1
    if b <= c <= a:
        return right-1
    return left

# Method to partition list
def partition(array, left, right, pi):
	swap(array, pi, right)
	pivot_value = array[right]
	store = left
	for i in range(left, right):
		if array[i] <= pivot_value:
			swap(array, store, i)
			store = store+1
	swap(array, store, right)
	return store

# Method to swap elements in list
def swap(array, pos1, pos2):
	array[pos1], array[pos2] = array[pos2], array[pos1]
	return array

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
def quickSort(array, left, right):
	if len(array) < 10:
		insertion_sort(array)
	if left < right:
		pi = median3(array, left, right) 
		pivot_index = partition(array, left, right, pi) 
		quickSort(array, left, pivot_index-1) 
		quickSort(array, pivot_index+1, right)

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
	# Quick Sort
	quick_list_1 = [-21, 22, 48, 74, 92, 7, 28, 19, -21, 29, 39, 44, 76, 46]
	quick_list_2 = [5, 3, 2, 1, -91, 64, 27, 88, 91]
	quick_list_3 = [-81, 22, 45, 27, 34, 98, 67]

	n1 = len(quick_list_1)
	n2 = len(quick_list_2)
	n3 = len(quick_list_3)

	quickSort(quick_list_1,0,n1-1) 
	print ("Sorted array is:") 
	print(quick_list_1)

# ------------
# Test
# ------------
def main():
	# Create binary files
	create_sorted_bin()
	create_reverse_bin()
	create_random_bin()

	# Collect file_name to be read
	file_name = collect_input()
	original_1 = read_bin(file_name)
	print(f'Array Ordered: {is_ordered(original_1)}')

	# # Time insertion sort
	# time_1 = time.clock()
	# original_1 = insertion_sort(original_1)
	# elapsed_time = time.clock() - time_1
	# print(f'Array Ordered: {is_ordered(original_1)}, Time Taken: {format(elapsed_time, ".2e")}')
	# print(original_1)


if __name__ == '__main__':
	main()

