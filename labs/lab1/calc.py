import numpy as np 

# Problem 1
p1_list1 = [.01894, .01991, .01996, .02013, .01968, .02038, .01870, .01967, .01984, .02058]
p1_list2 = [.1106, .1093, .1108, .1097, .1115, .1104, .1106, .1095, .1108, .1096]
p1_list3 = [.8490, .8612, .8442, .8626, .8534, .8580, .8468, .8622, .8468]

# Problem 2
p2_list1 = [.05905,.06113, .06126, .06110, .06120, .06099, .06094, .06068, .06074, .06110]
p2_list2 = [.3111, .2310, .2300, .2305, .2262, .2297, .2286, .2298, .2263, .2266]
p2_list3 = [.9049, .9000, .9012, .9029, .9019, .8979, .9037, .8992, .8989, .9017]

# Problem 3
p3_list1 = [.3588, .3566, .3558, .3552, .3537, .3540, .3547, .3544, .3534, .3548]
p3_list2 = [.7301, .7238, .7293, .7261, .7285, .7237, .7277, .7245, .7303, .7234]
p3_list3 = [1.509, 1.492, 1.506, 1.511, 1.507, 1.507, 1.505, 1.508, 1.508, 1.507]
 
# Problem 4
p4_list1 = [.07120, .07288, .07102, .07325, .07159, .07048, .07327, .07256, .07122, .07248]
p4_list2 = [.1440, .1427, .1468, .1422, .1445, .1432, .1450, .1416, .1475, .1431]
p4_list3 = [.2937, .2880, .2877, .2894, .2825, .2901, .2856, .2838, .2914, .2856]


def average(array):
	average = np.average(array)
	print(f'Run Time: {format(average, ".2e")}')


#--------
# Main
#--------
def main():
	average(p1_list1)
	print(f'Std Dev 1: {np.std(p1_list1)}')
	average(p1_list2)
	print(f'Std Dev 2: {np.std(p1_list2)}')
	average(p1_list3)
	print(f'Std Dev 3: {np.std(p1_list3)}')
	print()

	average(p2_list1)
	print(f'Std Dev 1: {np.std(p2_list1)}')
	average(p2_list2)
	print(f'Std Dev 2: {np.std(p2_list2)}')
	average(p2_list3)
	print(f'Std Dev 3: {np.std(p2_list3)}')
	print()

	average(p3_list1)
	print(f'Std Dev 1: {np.std(p3_list1)}')
	average(p3_list2)
	print(f'Std Dev 2: {np.std(p3_list2)}')
	average(p3_list3)
	print(f'Std Dev 3: {np.std(p3_list3)}')
	print()

	average(p4_list1)
	print(f'Std Dev 1: {np.std(p4_list1)}')
	average(p4_list2)
	print(f'Std Dev 2: {np.std(p4_list2)}')
	average(p4_list3)
	print(f'Std Dev 3: {np.std(p4_list3)}')
	print()

if __name__ == '__main__':
	main()