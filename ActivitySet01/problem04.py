# Co0nditional Execution
'''
hrs = input("Enter Hours:")
rate=input("Enter rate:")
hrs=float(hrs)
rate=float(rate)
if hrs<=40:
    pay=hrs*rate
else:
    pay=hrs*rate
    pay=pay + ((hrs-40)*(rate*0.5))
    print(pay)'''
    
#or another type
hrs = input("Enter Hours:")
rate=input("Enter rate:")
hrs=float(hrs)
rate=float(rate)
if hrs<=40:
    pay=hrs*rate
else:
    pay=40*rate
    pay=pay + ((hrs-40)*(rate*1.5))
    print(pay)
    