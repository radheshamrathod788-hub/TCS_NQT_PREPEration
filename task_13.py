num1=int(input(":"))
num2=int(input(":"))
num3=int(input(":"))
num4=int(input(":"))

if num1>num2 and num1>num3 and num1>num4:
    print(num1,"is largest")
elif num2>num1 and num2>num3 and num2>num4:
    print(num2,"is largest")
elif num3>num1 and num3>num2 and num3>num4:
    print(num3,"is largest")
else:
    print(num4,"is grater")