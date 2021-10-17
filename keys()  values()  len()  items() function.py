#Programmer Sadiq
#By@Sadiqul Islam
#Use of dictionary


#dict() function
#dict() -> new empty dictionary
#dict(mapping) -> new dictionary initialized from a mapping object

d = {'Name':'Sadiqul Islam','Roll No': 900243,'Dept':'Computer'}#dictionary

d['Semester'] = '6th' 
d['Group'] = 'B'
d['Age'] = '22'
#d.update({'name': 'Mahbub','age': 19,'phone': '7748363'})


#del d['Group'] #use of del function
#age = d.pop('Age') #use of pop() function


print(d)
#print(age)
#print(d.get('Phone','Not Found!'))
#print(len(d)) #use of len() function
#print(d.keys())
#print(d.values())
#print(d.items())

#for key in d:
    #print(key)

for key,value in d.items():
    print(key,value)
