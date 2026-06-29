#what is class?
#a class is a bluprint for creating objects.
#it defines the preperties (attributes) and
#behaviouts(methods,fuction) that object fo
#of that class will have.

# init  function means costructior
#constructor means class object
#without object access

class DATA :
    def __init__(self,name,age):
        self.name=name #attribute
        self.age=age 
    def introduction(self,name):
        print(f"my name is  {self.name} and my age is {self.age}")
        print("my name is",name)
d1=DATA("radhe",21)
d1.introduction("radhe")
d1.introduction("shyam")