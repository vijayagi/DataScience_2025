"""IN DICTINARY TAKING TUPLES AS VALUES"""



groceries={"fruits":("mango","apple"),"vegetables":("tomato")}
print(groceries["fruits"])

#self function
#self represents the instance of the class(the object itself)
#automatically passsed when we call the object
#with self we can acess attributes and methods of objects
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age



    def introduction(self):
        print(f"hi i am {self.name} and i am {self.age} years old")

s1=student('santhosh',23)
s1.introduction()


