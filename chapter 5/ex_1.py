count = 0
total = 0
try:
    
    while True:
        x = input ('Enter a number: ')
        if x == 'done':
            break
        else:
            count = count + 1
            total = total + int(x)
            average = total/count
    print(total, count, average)
except:
    print ('invalid input')

        





