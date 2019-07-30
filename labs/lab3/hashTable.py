import math
import re

class HashSet:
	# Constructor
	def __init__(self, table_size):
		# Check next power of 2
		self.m_count = self.next_power_of_2(table_size)
		self.m_table = [(None, None)]*self.m_count

	# Inserts value into set
	def add(self, value):
		# Get/Check load factor
		l = self.loadFactor()
		if l > 0.8:
			self.resizeTable()

		# See if value is in set
		in_set, index = self.find(value)

		if in_set == False:
			self.m_table[index] = (value, False)	
		return 

	# Returns true if value is present in set
	def find(self, value):
		# Calculate hash for value
		index = self.calculateIndex(value)

		# Get tuple at index
		table_val, is_nil = self.m_table[index]

		count = 1
		while(count != self.m_count+1):
			# If value is in set return true
			if table_val == value and is_nil == False:
				return True, index

			# If array value is empty return false
			elif is_nil == None:
				return False, index

			# If array has that value but is NIL return false
			elif table_val == value and is_nil == True:
				return False, index

			# Else keep searching next index
			else:
				i = self.probingFunction(count)
				index = (index + i) % self.m_count
				table_val, is_nil = self.m_table[index]
				count += 1
		return False, index

	# Removes given value from set
	def remove(self, value):
		in_set, index = self.find(value)
		if in_set == True:
			self.m_table[index] = (value, True)
		return

	# Returns next power 2 greater than or equalt to x
	def next_power_of_2(self, x):
		return 1 if x == 0 else 2**math.ceil(math.log2(x))

	# Returns num values in table
	def count(self):
		count = 0
		for tup in self.m_table:
			value, is_nil = tup
			if is_nil == False:
				count += 1

		return count

	# Returns load factor of table
	def loadFactor(self):
		n = self.count()
		return n / self.m_count

	def probingFunction(self, i):
		return int(((math.pow(i, 2) + i )/ 2))

	def calculateIndex(self, value):
		hash_val = hash(value)
		return hash_val % self.m_count

	# Resizes table and re-hash/insert elements
	def resizeTable(self):
		# Create new array twice the size
		self.m_count = self.m_count * 2
		new_mtable = [(None, None)]*self.m_count

		# Iterate through old table
		for value in self.m_table:
			# Get tuple from old table
			val, nil = value

			if nil != None or nil != True:

				# Calculate new index for val
				index = self.calculateIndex(val)

				# Get tuple at new index
				table_val, is_nil = new_mtable[index]

				count = 1
				while(count != self.m_count+1):
					# If spot is empty add new value
					if is_nil == None or is_nil == True:
						new_mtable[index] = (val, nil)
						break

					# Else keep searching next index
					else:
						i = self.probingFunction(count)
						index = (index + i) % self.m_count
						table_val, is_nil = new_mtable[index]
						count += 1

		self.m_table = new_mtable[:]
		return

# ------------------
# Main 
# ------------------
def main():
	# -----------------
	# Trump Speech
	# -----------------
	trump_hash = HashSet(50)
	trump_test_set = set()
	word_count = set()


	with open('trump_speech.txt', 'r') as file:
		count = 0
		for word in file.read().split():
			count += 1
			word_count.add(word)
			
			stripped_word = re.sub(r'\W+', '', word)
			trump_test_set.add(stripped_word)
			trump_hash.add(stripped_word)

		print(f'The original number of words are: {trump_hash.count()}')
		print(f'Built in set stripped characters: {len(trump_test_set)}')
		print(f'Built in set no stripped characters: {len(word_count)}')
		print(f'Count of words : {count}')

		print(trump_test_set)



if __name__ == '__main__':
	main()


	# # -----------------
	# # Test operations
	# # -----------------

	# # Create a hashset with table size 10
	# h = HashSet(5)
	# print(h.m_table)

	# # Calculate the count of filled values
	# print(f'The count is currently: {h.count()}')

	# # Determine load factor for table
	# print(f'Load factor: {h.loadFactor()}')

	# # -----------------
	# # Test Add
	# # -----------------

	# # Add value to table
	# h.add(16)
	# print(h.m_table)

	# # Add another value to table
	# h.add(23)
	# print(h.m_table)

	# # Add same value to table
	# h.add(23)
	# print(h.m_table)

	# # Add another value
	# h.add(32)
	# print(h.m_table)

	# # Add another value
	# h.add(40)
	# print(h.m_table)

	# # Add another value
	# h.add(48)
	# print(h.m_table)

	# # Add another value
	# h.add(56)
	# print(h.m_table)

	# # Add another value
	# h.add(64)
	# print(h.m_table)

	# # Add another value
	# h.add(72)
	# print(h.m_table)

	# # Add another collision value
	# h.add(80)
	# print(h.m_table)

	# # Add another collision value
	# h.add(0)
	# print(h.m_table)

	# # -----------------
	# # Test Find
	# # -----------------

	# # First index
	# print(f'Find result: {h.find(16)}')

	# # Next index
	# print(f'Find result: {h.find(23)}')

	# # Next ith index
	# print(f'Find result: {h.find(64)}')

	# # Last index
	# print(f'Find result: {h.find(72)}')
	# print(f'Find result: {h.find(80)}')

	# # Value not in set
	# print(f'Find result: {h.find(84)}')
	# print(f'Find result: {h.find(0)}')



	# # -----------------
	# # Test Remove
	# # -----------------

	# # Remove index 0
	# h.remove(16)
	# print(f'Remove result:\n {h.m_table}')

	# # Remove next value
	# h.remove(23)
	# print(f'Remove result:\n {h.m_table}')

	# # Remove next value
	# h.remove(64)
	# print(f'Remove result:\n {h.m_table}')

	# # Remove next value
	# h.remove(72)
	# print(f'Remove result:\n {h.m_table}')

	# # Remove same value
	# h.remove(72)
	# print(f'Remove result:\n {h.m_table}')

	# -----------------
	# Test-Case 2
	# -----------------
	# Create hash set
	# h2 = HashSet(2)

	# # Add a value
	# h2.add(2)
	# print(h2.m_table)

	# # Add some more values
	# h2.add(4)
	# h2.add(1234)
	# h2.add(-21)
	# h2.add(92)
	# print(h2.m_table)

	# # Remove some values
	# h2.remove(4)
	# h2.remove(92)
	# print(h2.m_table)

	# # Find some values
	# print(h2.find(4))
	# print(h2.find(92))
	# print(h2.find(1234))

	# # Put some values back in
	# h2.add(4)
	# print(h2.m_table)

	# # Add some collision values
	# h2.add(12)
	# print(h2.m_table)

	# print(f'The current count of the table is {h2.count()}')
