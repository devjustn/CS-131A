'''
User inputs number of tossed to perform, outputs result of each toss
'''

import random
H = "Heads"
T = "Tails"
QUERY = "Enter the number of tosses to perform: "

print(QUERY, end = '')
frequency = int(input())

for i in range(frequency):
	if random.randint(0,1) == 0:
		print(H)
	else:
		print(T)
