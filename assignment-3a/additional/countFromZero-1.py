# output this many numbers 
n = int(input("How many numbers to output? "))

number = 1 # start with this number
for i in range (0, n):
  print(number, end=" ") # for separation
  number += 1 # go to the next number
 
print() # skip to the next line