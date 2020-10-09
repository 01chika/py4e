hours = input('Enter hours: ')
try:
    h = int(hours)
    rate = input ('Enter rate: ')
    r = int(rate)
    if h>40:
        pay = (h-40)*(r*1.5) + (40*r)
        print(pay)
    else:
        pay = h*r
        print(pay)
except:
    print('Error, please enter a numeric input')

