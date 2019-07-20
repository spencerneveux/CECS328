import time
import random
import math

#---------------
# Set up
#---------------
def menu():
	user_input = input("1) Quit\n2) Time Freddy's\n3) Time Susie's\n4) Time Johnny's\n5) Time Sally's\n")
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
	max_num = 0
	for i in range(0, len(array)):
		for j in range(i, len(array)):
			this_sum = 0
			for k in range(i, j+1):
				this_sum += array[k]
			if this_sum > max_num:
				max_num = this_sum
	return max_num
			
def susie(array):
	max_num = 0
	for i in range(0, len(array)):
		this_sum = 0
		for j in range(i , len(array)):
			this_sum += array[j]
			if this_sum > max_num:
				max_num = this_sum
	return max_num

def johnny(array, left, right):
	if right < 0: 
		return 0
	if left == right:
		if array[left] > 0:
			return array[left]
		return 0

	# Split array in half and find each halfs max sum
	center = math.floor((left + right) / 2)
	max_left_sum = johnny(array, left, center)
	max_right_sum = johnny(array, center+1, right)

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
	for i in range(center+1, right+1):
		right_border += array[i]
		if right_border > max_right_border:
			max_right_border = right_border

	# the max sum is the largest of the three
	return max(max_left_sum, max_right_sum, max_left_border+max_right_border)

def sally(array):
	max_num = 0
	this_sum = 0
	for i in range(0, len(array)):
		this_sum += array[i]
		if this_sum > max_num:
			max_num = this_sum
		elif this_sum < 0:
			this_sum = 0
	return max_num

#---------------
# Test-Main
#---------------
def test_main():
	array_1 = [11, -76, 34, 44, -98, 1, 21, -10, 9, 100]
	array_2 = [21, 84, -74, 18, 92, -32, 66, 38, 91, -21, 1]
	array_3 = []
	array_4 = [-10, -94, -100, -23, -43, -75, -23, -86, -11, -32]
	array_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	array_6 = [21, 85, 38, 45, 24, 68, 22, 45, 92, 12]

	# Testing Freddy
	max_sum = freddy(array_1)
	print(f'Freddy Max Sum = {max_sum}')
	max_sum = freddy(array_2)
	print(f'Freddy Max Sum = {max_sum}')
	max_sum = freddy(array_3)
	print(f'Freddy Max Sum = {max_sum}')
	max_sum = freddy(array_4)
	print(f'Freddy Max Sum = {max_sum}')
	max_sum = freddy(array_5)
	print(f'Freddy Max Sum = {max_sum}')
	max_sum = freddy(array_6)
	print(f'Freddy Max Sum = {max_sum}')
	print()

	# Testing Susie
	max_sum = susie(array_1)
	print(f'Susie Max Sum = {max_sum}')
	max_sum = susie(array_2)
	print(f'Susie Max Sum = {max_sum}')
	max_sum = susie(array_3)
	print(f'Susie Max Sum = {max_sum}')
	max_sum = susie(array_4)
	print(f'Susie Max Sum = {max_sum}')
	max_sum = susie(array_5)
	print(f'Susie Max Sum = {max_sum}')
	max_sum = susie(array_6)
	print(f'Susie Max Sum = {max_sum}')
	print()

	# Testing johnny
	max_sum = johnny(array_1, 0, len(array_1)-1)
	print(f'Johnny Max Sum = {max_sum}')
	max_sum = johnny(array_2, 0, len(array_2)-1)
	print(f'Johnny Max Sum = {max_sum}')
	max_sum = johnny(array_3, 0, len(array_3)-1)
	print(f'Johnny Max Sum = {max_sum}')
	max_sum = johnny(array_4, 0, len(array_4)-1)
	print(f'Johnny Max Sum = {max_sum}')
	max_sum = johnny(array_5, 0, len(array_5)-1)
	print(f'Johnny Max Sum = {max_sum}')
	max_sum = johnny(array_6, 0, len(array_6)-1)
	print(f'Johnny Max Sum = {max_sum}')
	print()

	# Testing sally
	max_sum = sally(array_1)
	print(f'Sally Max Sum = {max_sum}')
	max_sum = sally(array_2)
	print(f'Sally Max Sum = {max_sum}')
	max_sum = sally(array_3)
	print(f'Sally Max Sum = {max_sum}')
	max_sum = sally(array_4)
	print(f'Sally Max Sum = {max_sum}')
	max_sum = sally(array_5)
	print(f'Sally Max Sum = {max_sum}')
	max_sum = sally(array_6)
	print(f'Sally Max Sum = {max_sum}')

	
#---------------
# Main
#---------------
def main():
	user_input = ''

	while user_input != '1':
		# Display Menu/Collect input
		user_input = menu()
		print(f'You chose: {user_input}')

		if user_input == '1':
			print('Exiting')

		else:

			# Collect seed and array size
			seed, size = collect_input()
			print(f'Seed: {seed}, Size: {size}')

			# Create the array 
			array = create_array(seed, size)

		if user_input == '2':

			# Run Freddy algorithm
			time_1 = time.clock()
			max_num	= freddy(array)
			elapsed_time = time.clock() - time_1
			print(f'Max sum {max_num}, Elapsed Time {format(elapsed_time, ".3e")}')

		elif user_input == '3':

			# Run Susie algorithm
			time_1 = time.clock()
			max_num = susie(array)
			elapsed_time = time.clock() - time_1
			print(f'Max sum {max_num}, Elapsed Time {format(elapsed_time, ".3e")}')

		elif user_input == '4':

			# Run Johnny algorithm
			time_1 = time.clock()
			max_num = johnny(array, 0, len(array)-1)
			elapsed_time = time.clock() - time_1
			print(f'Max sum {max_num}, Elapsed Time {format(elapsed_time, ".3e")}')

		elif user_input == '5':
			# Run Sally algorithm
			time_1 = time.clock()
			max_num = sally(array)
			elapsed_time = time.clock() - time_1
			print(f'Max sum {max_num}, Elapsed Time {format(elapsed_time, ".3e")}')



if __name__ == '__main__':
	main()
