#Programmer Sadiq
#By@Sadiqul Islam
#Python - Access Dictionary Items



#Accessing Items
'''
-You can access the items of a dictionary by referring to its key name, inside square brackets:
-Example: Get the value of the "dept" key. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }

obj = student['dept']
print(obj)

'''There is also a method called get() that will give you the same result'''
x = student.get('dept')
print(x)

#Get Keys
'''
-The keys() method will return a list of all the keys in the dictionary.
-Example: Get a list of the keys '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
x = student.keys()
print(x)
'''
-The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
-Example: Add a new item to the original dictionary, and see that the keys list gets updated as well'''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
x = student.keys()
print(x) #before the change

student['roll'] = '900243'
print(x) #after the change

#Get Values
'''
-The values() method will return a list of all the values in the dictionary.
-Example: Get a list of the values. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
x = student.values()
print(x)

'''
-The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
-Example: Make a change in the original dictionary, and see that the values list gets updated as well'''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
x = student.values()
print(x) #before the change

student ['admission'] = 2018
print(x) #after the change

#Check if Key Exists
'''
-To determine if a specified key is present in a dictionary use the in keyword.
-Example: Check if "dept" is present in the dictionary. '''

student = {
        'name': 'Sadiqul Islam',
        'collage': 'TPI',
        'dept': 'CSE',
        'shift': '1st',
        'admission': 2017,
    }
if 'dept' in student:
    print("Yes, 'dept' is one of the keys in the student dictionary")

