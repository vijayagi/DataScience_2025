#tuple is ordered,unchangable and allow duplicate values
fruits=('apple','banana','cherry','kiwi')
vegies=('carrot','potato','tomato','carrot')
print('fruits in tuple datatype',fruits)
print('vegies in tulple datatype',vegies)
tuple1=('apple',) #when there is only one item in tuple
tuple2=('aplle')


#len and type of tuple
print('length of fruits',len(fruits))
print('type of fruits',type(fruits))


#indexing and slicing
print('we are going to practice indexing on fruits:',fruits)
print('fruits[1]',fruits[1])
print('fruits[-1]',fruits[-1])
print('fruits[1:3]',fruits[1:3])
print('fruits[-4:-1]',fruits[-4:-1])

#check apple is in fruits
x=input('give input to check item in fruits')
if x in fruits:
    print(f"{x} is in fruits")
else:
    print(f"{x} is not in fruits")

#adding tuple1 & tuple2
tuple2=('orange',)
fruits+=tuple2
print(fruits)

list1=list(fruits)
list1.remove('orange')
fruits=tuple(list1)
print('after converting tuple to list and removing orange',fruits)

# unpacking tuple
red,yellow,small,green=fruits
print(red,yellow,small,green)
*red,yellow,green=fruits #* is used to allocate extra values in variables
print("values in variable *red",*red)

#looping in tuples
for x in fruits:
    print(x)
for i in range(len(fruits)):
    print(f"fruits{i}:",fruits[i])

i=0
while i <len(fruits):
    print(f"fruits{i}:",fruits[i])
    i+=1

#join tuple
join_tuple=fruits+vegies
print(join_tuple)

print(2*fruits) #it will print 2 times
 #tuple methods
print("count of apple in fruits",fruits.count('banana'))
print("index of apple in fruits",fruits.index('kiwi'))

