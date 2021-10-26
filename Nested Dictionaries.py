#Programmer Sadiq
#By@Sadiqul Islam
#Python - Nested Dictionaries


#Nested Dictionaries
'''
A dictionary can contain dictionaries, this is called nested dictionaries.
Example: Create a dictionary that contain three dictionaries.'''

Student_dict = {
    'student1': {
        'name': 'Imam',
        'roll': 101
        },
    'student2': {
        'name': 'Sohel',
        'roll': 102
        },
    'student3': {
        'name': 'Nur',
        'roll': 103
        }
    }

print(Student_dict)

'''
Or, if you want to add three dictionaries into a new dictionary:
Example: Create three dictionaries, then create one dictionary that will contain the other three dictionaries.'''

student1 = {
    'name': 'Jaman',
    'roll': 101
    }
student2 = {
    'name': 'Roman',
    'roll': 102
    }
student3 = {
    'name': 'Zubayer',
    'roll': 103
    }

Student_dict = {
    'student1': student1,
    'student2': student2,
    'student3': student3
    }

print(Student_dict)
