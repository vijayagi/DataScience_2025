# dictionary are used to store data values in key:value pairs
#dictionary is which is ordered,changebale and doed not allow duplicates
student1={'name':'santhosh','age':22,'gender':'male'}
print(student1)
print(type(student1))

#when we are using duplicate keys it will overwrite the previous key with new one
student2={'name':'santhosh','age':22,'gender':'male','age':32}
print(student2)

#length of dictionary
print(len(student1))

#accesing items
print('name:',student1['name'])
print('age:',student1.get('age'))  #get keyword to get the value

#getting keys and values
x=student1.keys()
print('keys before adding adress:',x)
student1['address']='hyd'
print(student1)
print('keys after adding adress:',x) #keys will change because it is the view of the dictionary
y=student1.values()
print('values :',y)
z=student1.items()
print('items in dictionary :',z)

if 'name' in student1:
    print(f'yes key values pair "name:{student1["name"]}"  is present in dictionary')

#change items
student1.update({'year':2025,'sports':'cricket'})
print('adding key "year" in student1',student1)
student1['year']=2024
print('changing value of key "year" in student1',student1)

#delete items
student1.pop('address')
print('after dleting address with pop()',student1)
student1.popitem()
print('after dleting last item with popitem()',student1)
student1['year']=2025
print('after adding year with key "year" in student1',student1)
del student1['year']
print('after deleting year with key "year" in student1',student1)

#for loop in dict
for x in student1:
    print('applying for loop in dict',x)
for x in student1:
    print('applying for loop in dict',student1[x])
for x in student1.items():
    print('applying for loop in dict with student1.items()',x)
for x,y in student1.items():
    print('applying for loop in dict with student1.items() and displaying x and y:',x,y)

#copying dict
student3=student1.copy()
#if we use dict3=dict1 it will create reference not copy that is the changes made in dict1 will be reflected in dict3 
print('copying dict with copy()',student3)
mydict=dict(student1)
print('copying dict with dict()',mydict)

#nested dict
students={'stu1':{'name':'santhosh','age':22},'stu2':{'name':'hemanth','age':21},'stu3':{'name':'venky','age':20}}
print(students)
students4={'students1':student1,'students2':student2}
print(students4)

#accessing items in nested loop
print('accessing items in nested loop "students[stu1][name]:"',students['stu1']['name'])

for x,obj in students.items():
    print('key:',x)
    for y in obj:
        print('keys in nested loop:',y)
        print('values in nested loop:',obj[y])

#clear dict
student1.clear()
print('after clearing dict',student1)