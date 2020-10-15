def computepay(h,r):
    hours = input('Enter hours: ')
    h = float(hours)
    rate = input('Enter rate: ')
    r = float(rate)
    if h>40:
        pay = (h-40)*(r*1.5) + (40*r)
        return pay
    else:
        pay = h*r
        return pay

p = computepay(h,r)
print("Pay",p)
