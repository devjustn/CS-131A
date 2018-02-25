print("How many rows to output? ", end="") 
n = int(input()) # output this many rows 

stars = 1 
skip = n - 1 
for i in range(0, n): 
  for j in range(0, skip): print(" ", end="")
  for j in range(0, stars): print("*", end="") 
  print() 
  stars += 2; 
  skip -= 1

stars = 2 * n - 3 
skip = 1
extraRows = n - 1
for i in range(0, extraRows): 
  for j in range(0, skip): print(" ", end="")
  for j in range(0, stars): print("*", end="") 
  print() 
  stars -= 2
  skip += 1