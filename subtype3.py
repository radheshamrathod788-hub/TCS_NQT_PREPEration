#function with argument + with return

def add(a,b,c): #10 20 30 
    c=a+b+c #60
    return a+b+c # 10+20+60=90
    #return c
a,b,c=map(int,input("enter the values:").split())

print("addition=",add(a,b,c))