import time
import random

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

# Freddies algorithm is not checking the last element!!
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

	# Run Sally algorithm
	sally(array)

	
if __name__ == '__main__':
	main()