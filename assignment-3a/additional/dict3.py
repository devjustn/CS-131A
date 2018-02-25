# This program shows how to delete dictionary entries and
# also how to delete an entire dictioary.
# The dictionary named dict has three entries initialized in it  
# whem it is created.  The del command is then used for
# one entry to remove the entry from the dictionary. 
# Then the .clear() method is used to remove all remaining
# entries from the dictionary.
# After that the del command is used on dict to completely
# remove the dictionary so that it no longer can be used
# in the program.
# The program displays an error, because the print
# function calls atempt to print entries that have
# been deleted from the dictionary.
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
