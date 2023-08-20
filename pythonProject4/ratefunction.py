hour=input("enter your hour:")
rate=input("enter yor rate:")
pay=float(hour)*float(rate)
#print("pay",pay)
#changing
def payable(rate1,pay1):
    return "payable",float(rate1) * float(pay1)
finalPay=payable(rate,hour)
print(finalPay)

