'''
Exercise 1: Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None. 
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
'''

def chop(t):
    del t[0]
    t.pop()

def middle(t):
    return t[1:len(t)-1]


m=[1,2,3,4,5]
chop(m)
print(m)
print(m)

n=[1,2,3,4,5,6]
print(middle(n))
print(n)