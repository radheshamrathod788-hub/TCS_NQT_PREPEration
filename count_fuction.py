#count()
#count() returns the number of times specifide value
#appears in the tuple or how many times it value reprst
tuple=(1,2,3,4,3,2,2,3)
print("number of count 3:",tuple.count(3))
print("number of count 2:",tuple.count(2))

search=2
count1=0

for i in tuple:
    if i==search:
        count1+=1
print("count of 2 =",count1)