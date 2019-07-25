import random
import struct
import time
from statistics import mean

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
	NUM_INTEGERS = 10000
	with open('random.bin', 'wb') as file:

		file.write(struct.pack('i', NUM_INTEGERS))

		for i in range(NUM_INTEGERS+1):
			file.write(struct.pack('i', random.randint(0, 100000)))

def create_sorted_bin():
	NUM_INTEGERS = 10000
	with open('sorted.bin', 'wb') as file:

		file.write(struct.pack('i', NUM_INTEGERS))

		for i in range(1, NUM_INTEGERS+1):
			file.write(struct.pack('i', i))

def create_reverse_bin():
	NUM_INTEGERS = 10000
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
def insertion_sort(array, left, right):
	for i in range(left+1, right+1):
		j2 = i-1
		temp = array[i]
		for j in range(i-1, left-2, -1):

			j2 = j
			if j == left-1:
				break

			if array[j] > temp:
				array[j+1] = array[j]
			else:
				break
		array[j2+1] = temp
	return array

# Quick Sort method
def quickSort(array, left, right):
	if (right-left) < 10:
		insertion_sort(array, left, right)
	if left < right:
		pi = median3(array, left, right) 
		pivot_index = partition(array, left, right, pi) 
		quickSort(array, left, pivot_index-1) 
		quickSort(array, pivot_index+1, right)

# ------------
# Buffer VM
# Methods to prepare virtual machine
# ------------
def buffer_insertion():
	array_sorted = read_bin('sorted.bin')
	for i in range(5):
		insertion_sort(array_sorted)

def buffer_quick():
	array_sorted = read_bin('sorted.bin')
	for i in range(5):
		quick_sort(array_sorted, 0, len(array_sorted)-1)

# ------------
# Test
# ------------
def main():
	# # Create binary files
	create_sorted_bin()
	create_reverse_bin()
	create_random_bin()

	# Collect file_name to be read
	file_name = collect_input()
	original = read_bin(file_name)

	# Make copies of original array
	insertion_array = original[:]
	quick_array = original[:]

	# # Time insertion sort
	time_i = []
	for i in range(10):
		print(f'Array Ordered: {is_ordered(insertion_array)}')
		time_1 = time.clock()
		insertion_array = insertion_sort(insertion_array, 0, len(insertion_array) -1)
		elapsed_time = time.clock() - time_1
		time_i.append(elapsed_time)
		print(f'Array Ordered: {is_ordered(insertion_array)}, Time Taken Insertion Sort: {format(elapsed_time, ".3e")}')
		insertion_array = original[:]
	print(f'Sorted time array {time_i}, Avg = {mean(time_i)}')

	# # Time quick sort
	time_q = []
	for i in range(10):
		print(f'Array Ordered: {is_ordered(quick_array)}')
		time_1 = time.clock()
		quickSort(quick_array, 0, len(quick_array) -1)
		elapsed_time = time.clock() - time_1
		time_q.append(elapsed_time)
		print(f'Array Ordered: {is_ordered(quick_array)}, Time Taken Quick Sort: {format(elapsed_time, ".2e")}')
		quick_array = original[:]
	print(f'Sorted time array {time_q}, Avg = {mean(time_q)}')

if __name__ == '__main__':
	main()

