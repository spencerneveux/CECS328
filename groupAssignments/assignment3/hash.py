v_1 = 32767
v_2 = 683870835
v_3 = "cecs328"

# Function to convert to hash value
def hash(byte_array):
	answer = 0
	for i in range(0, len(byte_array)):
		answer = byte_array[i] + 31*answer

	return answer

def int_to_bytes(num, size):
	val = num.to_bytes(size, byteorder='big')
	array = bytearray(val)
	return array
	

# Value 1 
val = int_to_bytes(v_1, 2)
print(hash(val))

# Value 2
val = int_to_bytes(v_2, 4)
print(hash(val))

# Value 3
val = bytearray(v_3.encode('ascii'))
for i in range(len(val)):
	print(val[i])




