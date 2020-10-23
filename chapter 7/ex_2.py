#Exercise 2: Write a program to prompt for a file name, and then read
#through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#values from these lines. When you reach the end of the file, print out
#the average spam confidence.

#-----------------------------------------------------------------------------

fname = input ('Enter file name: ')
fhand = open(fname)
count = 0
total_spamconf = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        line = line.rstrip()        #to remove whitespace (\n)
        zpos = line.find(' ')
        number = line[zpos+1:]
        x = float(number)
        total_spamconf = total_spamconf + x
    else:
        continue

    
average = total_spamconf/count
print('Average spam confidence:', average)
        
