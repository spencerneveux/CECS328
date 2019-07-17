import random
import struct

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
def isOrdered(array):
	for i in range(1, len(array)):
		if array[i-1] > array[i]:
			return False
	return True




# ------------
# Test
# ------------
def main():
	create_bin()
	file_name = collect_input()
	read_bin(file_name)

if __name__ == '__main__':
	main()