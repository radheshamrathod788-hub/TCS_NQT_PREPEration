#nested tuple meas tuple inside tuple

data=(
    ("aakash",90,45,"ram"),
    ("radhe",99,45,"sham"),
    ("rohan",43,43,"chauhan")
)
print(data)
for name,val,marks,hhg in data:
    print(name,"=",marks)