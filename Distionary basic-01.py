#Programmer Sadiq
#By@Sadiqul Islam
#Dictionary in python

dict = {}
print(dict)

dict['one'] = "This is one"
dict[2] = "This is two"

ndict = {'name': 'sadiqul', 'code': 4543, 'dept': 'sales'}
#print(dict['one'])
#print(dict[2])

#print(ndict)
#print(ndict.keys())
#print(ndict.values())

'''
-Dictionaries are used to store data values in key:value pairs.
-A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
-Dictionaries are written with curly brackets { }, and have keys and values
-Create and print a dictionary '''
student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
    }
print(student)


#Dictionary Items
'''
-Dictionary items are ordered, changeable, and does not allow duplicates.
-Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
-Example: Print the "dept" value of the dictionary '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
    }
print(student['dept'])


#Ordered or Unordered?
'''
-As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
-When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
-Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.'''

#Changeable
'''
-Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.'''

#Duplicates Not Allowed
'''
-Dictionaries cannot have two items with the same key.
-Example: Duplicate values will overwrite existing values. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
        'admission': 2018,
    }
print(student)

#Dictionary Length
'''
-To determine how many items a dictionary has, use the len() function.
-Example: Print the number of items in the dictionary. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
print(len(student))

#Dictionary Items - Data Types
'''
-The values in dictionary items can be of any data type.
-Example: String, int, boolean, and list data types. '''

student = {
        'name': ['Sadiqul Islam','Al-amin','Sohel Rana','Rakibul Islam'],
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
        'Technical': True,
    }
print(student)

#type()
'''
-From Python's perspective, dictionaries are defined as objects with the data type 'dict'
-Example: Print the data type of a dictionary. '''

student = {
        'name': ['Sadiqul Islam','Al-amin','Sohel Rana','Rakibul Islam'],
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
        'Technical': True,
    }
print(type(student))


