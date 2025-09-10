#list:where you can add multiple items
#ordered:items are in order
#changeable:you can change items
#allow duplicates
list1=['apple','banana','grapes','orange']
list2=['alan',20,'hyd']
list3=['apple','carrot','beetroot','apple']
print(list3,list1,list2)

#length,type of list
print(len(list1))
print(type(list3))


#indexing in list{0,1,2,3]
print('list1',list1[0],list1[1],list1[2],list1[3],list1)
print('negative index:',list1[-1],list1[-2])
print('prints ist and 2nd element:',list1[0:2])
print(list1[:3])  #strarts from 0 ends at index 2 (it doesn't include 3)
print('starsts from last but 3 ends at last but 1:',list1[-3:-1])  #starts from last but 3 element and ends at last but 1

#check if the object exists
if 'grapes' in list1:
    print('yes grapes exist in list1')
else:
    print('no grapes present in list1')


#replacing items,insert,append:
list1[1]='blackcurrent'
list1[1:2]=['blackcurrent','kiwi']
print('after replacing,list1',list1)
list1[1:3]=['custard']
print('after adding custad in 1:3',list1) # it replaced 1,2 positions
list1.insert(4,'kiwi')
list1.append ('blackcurrent')
print('after adding kiwi in 4th position and blackcurrent at end',list1)

#extend list2 and list3
list2.extend(list3)
print('list2',list2)
print('list3',list3)
print('after extending list2 and list3',list2)

#remove,pop,del,clear:
#removes the first occurence of specified item
list1.append('apple')
print('applying remove,pop,del,clear on list1:',list1)
list1.remove('apple')
print('after removing apple the first occurence',list1)
list1.pop(0)
list1.pop()
print('after pop 0 and last element',list1)
del list1[3]
print('after deleting 3rd element',list1)
list3=list1.copy()
list1.clear()
print('after clearing list1',list1)

#loop through list
list1=list3.copy()
for x in list1:
    print('looping through list1',x)

for i in range(len(list1)):
    print('looping through list1 through index',list1[i])

#while loop
i=0
while i <len(list1):
    print('while loop',list1[i])
    i+=1

#comprehension:
list4=[x for x in list1 ]
print('list4 got through comprehension',list4)



