#wrute program to calculate electricity bill.
if 500 unit used _pay RS 5 for each unit
if 700 unit used_pay RS 10 for each unit
if 1000 unit used_pay RS 15 for each unit
if more than 1000 unti used_pay RS 20 for each unit
def electricity_bill(n):
    if n<=500:
        print("you bill is Rs",n*5)
    elif n>500 and n<=700:
        print("you bill is Rs",n*10)
    elif n>700 and n<=1000:
        print("you bill is Rs",n*15) 
    elif n>1000:
        print("you bill is Rs",n*20)  
for i in range(4):
    c_name=input("enter the name of a costomer")  
    unit=int(input("enter the unit of electricity you have used"))  
electricity_bill(n)         