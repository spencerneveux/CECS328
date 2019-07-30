import math
import re

class HashSet:
	# Constructor
	def __init__(self, table_size):
		self.n = 0
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
			self.n += 1	
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
			self.n -= 1
		return

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

	# Returns next power 2 greater than or equalt to x
	def next_power_of_2(self, x):
		return 1 if x == 0 else 2**math.ceil(math.log2(x))

	# Returns count of elements in table
	def count(self):
		return self.n

	# Returns load factor of table
	def loadFactor(self):
		return self.n / self.m_count

	# Returns the probing function for current i
	def probingFunction(self, i):
		return int(((math.pow(i, 2) + i )/ 2))

	# Returns index 
	def calculateIndex(self, value):
		hash_val = hash(value)
		return hash_val % self.m_count

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
		print(f'Count of words : {count}')


if __name__ == '__main__':
	main()
