#!/usr/bin/python

dict = {'Name': 'John', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary
dict['Surname'] = "Appleseed"

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
