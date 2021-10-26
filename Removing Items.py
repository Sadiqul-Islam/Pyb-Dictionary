#Programmer Sadiq
#By@Sadiqul Islam
#Python - Remove Dictionary Items


#Removing Items
'''
-There are several methods to remove items from a dictionary:
-Example: The pop() method removes the item with the specified key name. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
        'roll': '900243',
        'gratuation': 2021,
    }

student.pop('roll')
print(student)

'''The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead). '''
student.popitem()
print(student)

'''The del keyword removes the item with the specified key name.'''
del student['admission']
print(student)

'''The clear() method empties the dictionary.'''
student.clear()
print(student)

'''The del keyword can also delete the dictionary completely.'''
del student
print(student) #this will cause an error because "thisdict" no longer exists.


