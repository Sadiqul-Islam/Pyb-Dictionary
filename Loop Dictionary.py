#Programmer Sadiq
#By@Sadiqul Islam
#Python - Loop Dictionaries


#Loop Through a Dictionary
'''
-You can loop through a dictionary by using a for loop.
-When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
-Example: Print all key names in the dictionary, one by one. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
        'roll': '900243',
        'gratuation': 2021,
    }

for x in student:
    print(x)

'''Print all values in the dictionary, one by one.'''
for x in student:
    print(student[x])

'''You can also use the values() method to return values of a dictionary.'''
for x in student.values():
    print(x)

'''You can use the keys() method to return the keys of a dictionary.'''
for x in student.keys():
    print(x)

'''Loop through both keys and values, by using the items() method.'''
for x, y in student.items():
    print(x,y)
