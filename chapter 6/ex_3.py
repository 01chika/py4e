#Exercise 3: Encapsulate this code in a function named count,
#and generalize it so that it accepts the string and the letter as arguments.

def count(w, l):    
    word = str(w)
    count = 0
    for letter in word:
        if letter == str(l):
            count = count + 1
    return count
   
z = count('abaaababbab', 'j')
print(z)
