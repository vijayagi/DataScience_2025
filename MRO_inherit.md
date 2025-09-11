1.In **multiple inheritance** where :



class A():

&nbsp;	def show(self):

&nbsp;		print("i am father")

class B():

&nbsp;	def show(self):

&nbsp;		print("i am mother")

class C(A,B):

&nbsp;	pass



obj=C()

obj.show()



**2.MRO:-Method Resolution order:**

MRO is the order in which python looks for the method/attribute in the inheritance hierarchy

check it using: print(C.mro())

C->A->B->obj



C3 linearization is the algorithm Python uses to generate the MRO.

* **Preserves local precedence order**

    If you write class D(B, C): ..., then B will always come before C in the MRO.



* **Monotonicity**



&nbsp;  A class’s MRO will always respect the MRO of its parent classes.



&nbsp;  EX: if B says its MRO is \[B, A, object], D must keep A after B.



* **No duplicates**



&nbsp;  Each class appears only once in the MRO











