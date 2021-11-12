'''
Exercise 1: Write a while loop that starts at the last character in the string 
and works its way backwards to the first character in the string, 
printing each letter on a separate line, except backwards.
'''

fruit = 'banana'

l=len(fruit)-1
while (l>=0):
    c=fruit[l]
    print(c)
    l-=1