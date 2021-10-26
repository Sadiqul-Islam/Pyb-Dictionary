#Programmer Sadiq
#By@Sadiqul Islam
#Python - Add Dictionary Items


#Adding Items
'''
-Adding an item to the dictionary is done by using a new index key and assigning a value to it.
-Example '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }

student['roll'] = '900243'
print(student)

#Update Dictionary
'''
-The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
-The argument must be a dictionary, or an iterable object with key:value pairs.
-Example: Add a color item to the dictionary by using the update() method. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
student.update({'gratuation': 2021})
print(student)
