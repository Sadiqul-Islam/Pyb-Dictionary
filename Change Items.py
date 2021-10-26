#Programmer Sadiq
#By@Sadiqul Islam
#Python - Change Dictionary Items

#Change Values
'''
-You can change the value of a specific item by referring to its key name:
-Example: Change the "admission" to 2018 '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }

student['admission'] = 2018
print(student)

#Update Dictionary
'''
-The update() method will update the dictionary with the items from the given argument.
-The argument must be a dictionary, or an iterable object with key:value pairs.
-Example: Update the "admission" of the car by using the update() method '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
student.update({'admission': 2018})
print(student)
