numbersList = [2, 3, 5, 7, 11, 13, 17]

listOfStrings = ["table", "chair", "door", "ceiling", "floor"]

#Task # 1 — print out each single element of the numbers list.  Each element should be printed on its own print line.
print("Task #1")
x = 0
y = 0
while x < len(numbersList):
  print(numbersList[x])
  x += 1
print('')

# Task 2 — print out all of the elements of the strings lists that are not pieces of furniture
print("Task #2")
print(listOfStrings[3:])
print('')


# Task # 3 — using slicing, print out all of the elements of the number list except the element in index 0, 
#the element in index 4 and the element in index 6 # only 3, 5, 7, 13
print("Task #3")
print(numbersList[1:4] + numbersList[5:6])
print('')

# Task # 4 — using slicing with positive values for indices print out only the last three elements of the strings list
print("Task #4")
print(numbersList[4:])
print('')

# Task # 5 — using slicing with negative values for indices print out only the last three elements of the strings list
print("Task #5")
print(numbersList[-3:])
print('')

# Task # 6 — using the if command and a true/false expression print out “Yes” if the number at the
# lowest index in the numbers list is less than the number at the highest index
print("Task #6")
if numbersList[0] < numbersList[len(numbersList) - 1]:
	print("Yes")
print('')

# Task # 7 — using the if command and true/false expressions print out “No” if the string at
# the lowest index in the string list is not the same string at the highest index
print("Task #7")
if listOfStrings[0] != listOfStrings[len(listOfStrings) - 1] :
  print("No")
print('')

# Task # 8 — print out all of the characters in the string at the lowest index in reverse order. 
# That is, the last character of the string should be printed first, the second to last character should be printed second,
# the third to last character should be printed third, ... , the first character should be printed last 
print("Task #8")
print(listOfStrings[0][::-1])
print('')