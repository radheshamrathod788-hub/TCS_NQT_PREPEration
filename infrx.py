#index fuction
'''indes ( ) returns the indes position of the 1st 
ocurrance'''

tuple=("radhe","ram","kishor")
print(tuple.index("radhe"))
print(tuple.index("kishor"))

number=0

for i in range(len(tuple)):
    if tuple[i]==number:
        print("index=",i)
        print(i)
        break

'''search=0
for i in tuple:
    if(tuple=="kishor"):
        print(i)
        break
'''