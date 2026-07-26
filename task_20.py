#ATM Withdraw
# requirment balance 10000
#withdral amount balace < 
# if balance < withdalmount:
        # print("transection sucsessfull")

balance=10000
user=int(input("inter withdrawal amont:"))
if user<= balance:
    print("transection successful")
    balance=balance-user
    print("avalable balance=",balance)

else:
    print("balance not available")
    print("avalable balance=",balance)
    