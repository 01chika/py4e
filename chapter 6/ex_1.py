#Exercise 1: Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.

word = 'Chika'
index = 4
while index >= 0:
    x = word[index]
    print(x)
    index = index - 1
