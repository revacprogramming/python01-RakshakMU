'''def computepay(h,r):
  if h < 40:
    pay = (h*r)
  else:
    pay = 40*r+((h-40)*(1.5*r))
  return pay 

hrs=input("Enter hrs : ")
h=float(hrs)
rate=input("Enter rate :")
r=float(rate)

pay = computepay(h,r)
print(pay)'''



'''def computepay(h, r):
    if h<=40:
        return h*r
    elif h>40:
        h1=h-40
        fee=40*r+h1*r*1.5
        return fee
hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))
p = computepay(hrs, rte)
print("Pay", p)'''



def computepay(h,r):
  
  if h<40:
    return h*r
  else:
    pay=40*r+((h-40)*1.5*r)
    return pay
h=float(input("Enter hrs"))
r=float(input("Enter rate"))    
p=computepay(h,r)
print(p)

#h=float(input("Enter hrs"))
#r=float(input("Enter rate")) these two cannot be written inside def function