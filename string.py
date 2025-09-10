#multiples string lines
print("""hi 
i am santhosh
i am practising python strings""")

#string as an array
text1="hello world"
print('text1[1]=',text1[1])

if "llo" in text1:
    print(True)

# length of string
print('length of text1',len(text1))
 #slicing
print('slicing from 2 to 5',text1[2:5])
print ('slice from -5 to -2',text1[-5:-2])
#modify strigs
print('upper case',text1.upper())
print('lower case',text1.lower())
#remove whitespace strip() function
text2="  iam santhosh  "
print('remove whitespace',text2.strip())

#split()function
text3="i am,santhosh,how are you"
print("splitting at ,",text3.split(","))

#replace()function
text5="dogs are cute"
print(text5.replace("dogs",'cats'))

#format or f string
age,number=21,2
print(f"iam {age} years old")
print(f"shop has {number} magoes")

#string methods
text4=text5.capitalize()
print(text4)

#boolean
print(bool('abc'))  #true
print(bool(0))  #false
