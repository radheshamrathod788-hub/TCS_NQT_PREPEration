#len()=== length of tuple==>.....

tuple=(1,2,3,4,5,6)
print("length =",len(tuple))
#6

#hard code for len function

count=0
for i in tuple:
    count+=1
print("using fo loop  length=",count)


count1=0
i=0
try:
    while True:
     tuple[i]

     count1+=1
     i+=1
except IndexError:
    pass
print("using while loop:",count1)