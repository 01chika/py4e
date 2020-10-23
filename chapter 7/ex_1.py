fname = input('Enter the name of file: ')
fhand = open(fname)
for line in fhand:
    line = line.upper()
    print(line)
