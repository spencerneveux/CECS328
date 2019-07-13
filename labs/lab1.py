import time
import random
import math

#---------------
# Set up
#---------------
def menu():
	user_input = input('1) Time Freddy\n2) Time Susie\n3) Time Johnny\n4) Time Sally\n5) Quit\n')
	return user_input

def collect_input():
	seed = input("Enter seed: ")
	size = input("Enter input size: ")
	return (seed, size)

def create_array(s, n):
	array = []
	random.seed(s)
	for i in range(int(n)):
		array.append(random.randint(-100, 100))
	return array


#---------------
# Algorithms 
#---------------

def freddy(array):
	time_1 = time.clock()
	max_num = 0
	for i in range(0, len(array)):
		for j in range(i, len(array)):
			this_sum = 0
			for k in range(i, j+1):
				this_sum += array[k]
			if this_sum > max_num:
				max_num = this_sum
	time_2 = time.clock()
	print(f'Max Sum = {max_num}, Time taken = {time_2 - time_1}')
	return max_num
			
def sophie(array):
	time_1 = time.clock()
	max_num = 0
	for i in range(0, len(array)):
		this_sum = 0
		for j in range(i , len(array)):
			this_sum += array[j]
			if this_sum > max_num:
				max_num = this_sum
	time_2 = time.clock()
	print(f'Max Sum = {max_num}, Time taken = {time_2 - time_1}')
	return max_num

def johnny(array, left, right):
	if left == right:
		if array[left] > 0:
			return array[left]
		return 0

	# Split array in half and find each halfs max sum
	center = math.floor((left + right) / 2)
	max_left_sum = johnny(array, left, center)
	max_right_sum = johnny(array, center+1, right)
	print(f'Left sum {max_left_sum} Right sum {max_right_sum}')

	# Find max starting at center moving left
	max_left_border = 0
	left_border = 0
	for i in range(center, left-1, -1):
		left_border += array[i]
		if left_border > max_left_border:
			max_left_border = left_border

	# Find max starting at center moving right
	max_right_border = 0
	right_border = 0
	for i in range(center, right+1):
		right_border += array[i]
		if right_border > max_right_border:
			max_right_border = right_border

	print(f'Max left: {max_left_sum} Max right: {max_right_sum}')

	# the max sum is the largest of the three
	return max(max_left_sum, max_right_sum, max_left_border+max_right_border)

def sally(array):
	time_1 = time.clock()
	max_num = 0
	this_sum = 0
	for i in range(0, len(array)):
		this_sum += array[i]
		if this_sum > max_num:
			max_num = this_sum
		elif this_sum < 0:
			this_sum = 0
	time_2 = time.clock()
	print(f'Max Sum = {max_num}, Time taken = {time_2 - time_1}')
	return max_num



#---------------
# Main
#---------------
def main():
	# Display Menu
	user_input = menu()
	print(f'You chose: {user_input}')

	# Collect seed and array size
	seed, size = collect_input()
	print(f'Seed: {seed}, Size: {size}')

	# Create the array 
	array = create_array(seed, size)
	print(array)

	# Run Freddy algorithm
	freddy(array)

	# Run Sophie algorithm
	sophie(array)

	# Run Johnny algorithm
	max_num = johnny(array, 0, len(array))
	print(f'Johnny max {max_num}')

	# Run Sally algorithm
	sally(array)


if __name__ == '__main__':
	main()