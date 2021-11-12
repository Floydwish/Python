'''
Exercise 3: Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments.
'''

def count(strings,letter):
    count=0
    for c in strings:
        if c==letter:
            count+=1
    return count

print(count('banana','a'))
