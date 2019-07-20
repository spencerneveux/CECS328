import random
import struct

NUM_INTEGERS = 1000

with open('file.bin', 'wb') as file:

	file.write(struct.pack('i', NUM_INTEGERS))

	for i in range(NUM_INTEGERS):
		file.write(struct.pack('i', random.randint(0, 1000000000)))

