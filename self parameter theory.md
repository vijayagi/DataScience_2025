**self in class**:

"it refers to the current instance(object) of the class"

* when you create class it is like you create a blueprint with many resources in that
* you can create instances(objects) to access the resources.



**Instance variables:**

these are the variables created in constructor and when we invoke self those variable can attach to that object through the reference(self)



**BY this each object has own values for instance variables.**



let's take an example to observe:

**class** kid:

&nbsp;	**def** \_\_init\_\_(self,name,toy):

&nbsp;		**self**.name=name

&nbsp;		**self**.toy=toy

&nbsp;	

&nbsp;	**def** show\_toy(self):

&nbsp;      	    print(f"My name is {**self**.name} and I play with {**self**.toy}")



kid1 = Kid("Santhosh", "Car")

kid2 = Kid("Ravi", "Ball")



kid1.show\_toy()  # My name is Santhosh and I play with Car

kid2.show\_toy()  # My name is Ravi and I play with Ball



**Explanation:**

here there are many kids and have many toys ; Santhosh has car and ravi has ball

* In kid1 object because of self name(Santhosh) and toy(car) are attached to kid1 obj and **"this solely belongs to kid1"**
* here when kid1 invoke show\_toy() because of self, the instance variables(name, toy) are already allocated to func() and they are going to print which are solely kid1's



**conclusion :"self is created to remove the confusion of whose data it is"**





