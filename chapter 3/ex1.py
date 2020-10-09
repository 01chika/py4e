score = input('Enter score: ')
try:
    if float(score)>=0.9 and float(score)<=1.0:
        print('A')
    elif float(score)>=0.8 and float(score)<0.9:
        print('B')
    elif float(score)>=0.7 and float(score)<0.8:
        print('C')
    elif float(score)>=0.6 and float(score)<0.7:
        print('D')
    elif float(score)<0.6 and float(score)>=0.0:
        print('F')
    else:
        print('Out of range')
except:
    print('Input numeric value')
