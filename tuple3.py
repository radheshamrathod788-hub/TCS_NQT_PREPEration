#can i declare tuple inside list
#yes
#you also can print the data as tuple()format
list=[1,2,3]
print(type(list))
data=[
    ("studen",33)
]
print(data)
print(type(data))

#if you print data in tupe them you use the for loop
#for loop print your value in tuple

for i in data:
    print(i)
data.append(("radhe"))
print(data)