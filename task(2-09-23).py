import re

#returns a match object if there is any match in the string
print(re.match(r'\d+','7abc'))
txt1="i am nani7"
print (re.search(r'\d+',txt1))

#findall returns a list containing all matches
#\A special sequence starts at beginning
txt2="i am santhosh1234"
print(re.findall(r'\Ai am',txt2))
print(re.findall(r'\d+',txt2))

#in re we use + and * as some special characters escape sheilds our text so it returns the string as it is
text3='i love c++'
pattern=re.escape('c++')
print(pattern) #returns c\+\+ takes + as different character

#sub: it is substitute function
text4 = "I like cats. cats are cute."
new_text = re.sub(r"cats", "dogs", text4)
print(new_text)


