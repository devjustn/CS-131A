# This program demonstrates how to update a dictionary.
# The dictionary named dict is initialize with keys and
# values when it is fist made.  Then, after the dictionary
# is initilized, one entry is changed in the dictionary,
# and one entry is added to the dictionary that was not
# in the dictionary when it was made.

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
