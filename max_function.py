tuple=(1,2,3,4,5,6,7,8,9,777,666,5,4,4,44444)
print("max=",max(tuple))

#hard code logic for max fuction in tuple

maxvalue=tuple[1]
for i in tuple:
    if i>maxvalue:
        maxvalue=i
print("max value using for loop=",maxvalue)