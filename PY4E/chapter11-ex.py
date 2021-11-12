'''
Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the
user to enter a regular expression and count the number of lines that matched the regular
expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$

'''
import re

def grep():
    exp=input('Enter a regular expression: ')
    fname='mbox.txt'
    try:
        fhand=open(fname)
    except:
        print('Can not open file: ',fname)
        exit()

    lst=list()
    count=0
    for line in fhand:
        line=line.rstrip()
        lst=re.findall(exp,line)
        if len(lst)>0:
            count+=1
    print('mbox.txt had %d lines that matched %s' %(count,exp))


#grep()


'''
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772

Extract the number from each of the lines using a regular expression and the findall() method.
Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
'''

import re
def calAverage():
    fname=input('Enter file: ')
    try:
        fhand=open(fname)
    except:
        print('Can not open file: ',fname)
        exit()
    summer=0
    count=0
    for line in fhand:
        line=line.rstrip()
        lst=re.findall('^New Revision: ([0-9]+)',line)
        for s in lst:
            summer+=int(s)
            count+=1
    print(summer//count)

#calAverage()


import re
def calSum():
    fname=input('Enter file: ')
    try:
        fhand=open(fname)
    except:
        print('Can not open file: ',fname)
        exit()
    summer=0
    count=0
    for line in fhand:
        line=line.rstrip()
        lst=re.findall('([0-9]+)',line)
        for s in lst:
            summer+=int(s)
    print(summer)

calSum()


'''
fhand=open('regex_sum_1359120.txt')
summer=0
for line in fhand:
    line=line.rstrip()
    lst=re.findall('([0-9]+)',line)
    for s in lst:
        summer+=int(s)
print(summer)
'''
