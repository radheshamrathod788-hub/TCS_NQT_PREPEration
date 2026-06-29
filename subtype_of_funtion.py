#sub type of function
#function with argument
#argument==> variable refrence variable object

def printname(name):
    print("my name is:",name)

printname("radhe")

def add(a,b):
    c=a+b
    print(c)

#add(30,64)
x,y=map(int,input("enter 2 value and y:").split())
add(x,y)