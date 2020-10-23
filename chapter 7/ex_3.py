fname = input('Enter name of a file: ')
try:
    if fname=='na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punkd!')
        quit()
    fhand = open (fname)
except:
    print ('file not found in directory')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

