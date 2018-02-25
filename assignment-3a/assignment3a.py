'''
Uses existing dictionary and updates entries by giving values for any existing key
Allow user to add new entries
'''

student = {'first name':'', 'last name':'', 'student_id':''}
CONTINUE_QUERY = "Add more to the dictionary (Y or y for yes)"
INFO_TYPE_QUERY = "enter a kind of information to add:"
VALUE_QUERY = "enter the value for the information to add:"

# Traverse dictionary and take in user input as a value for each key
def traverseD():
	for i in student:
		print('Enter', i, sep = ' ')
		student[i] = input()

# Display key and value
def displayD():
	print()
	print()
	for i in student:
		print(i,': ', student[i], sep = '')
	print()
	print()

# Add new key-value pair to dictionary
def newPairD():
	print(INFO_TYPE_QUERY)
	inKey = input()
	student[inKey] = ''
	print(VALUE_QUERY)
	inValue = input()
	student[inKey] = inValue

# Continue to ask for key-value pairs user agrees to continue
def main():
	print()
	traverseD()
	displayD()
	print(CONTINUE_QUERY)
	shouldContinue = input().lower() 
	while shouldContinue == 'y':
		newPairD()
		displayD()
		print(CONTINUE_QUERY)
		shouldContinue = input()
	displayD()

main()
