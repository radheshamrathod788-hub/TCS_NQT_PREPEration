#print 10 numbers without any loop

def print_10_number(number):
    if number>10:
        return  # or exit
    print(number)              
    print_10_number(number+1)       
print_10_number(number=1)        


'''if we call funtion in fuction then it repeate multiple times'''

list(map(print,range(1,11))) #fuction()
print(type(list))
print(id(list))#address or memory location

#map(key,value)