'''
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count 
how many messages have come from each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

'''

def countemailaddr():
    try:
        fname=input('please enter a file name:')
        fhand=open(fname)
    except:
        print('Can not open the file: ', fname)
        exit()
    mailcount=dict()
    for line in fhand:
        line=line.rstrip()
        if len(line)==0 or line.startswith('Author')==False:  continue
        words=line.split()
        if words[1] not in mailcount:
            mailcount[words[1]]=1
        else:
            mailcount[words[1]]+=1
    print(mailcount)

#countemailaddr()


'''
Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, look through the dictionary 
using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and 
print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195

'''
def countEmailAddrAndFindMax():
    try:
        fname=input('please enter a file name:')
        fhand=open(fname)
    except:
        print('Can not open the file: ', fname)
        exit()
    mailcount=dict()
    for line in fhand:
        line=line.rstrip()
        if len(line)==0 or line.startswith('Author')==False:  continue
        words=line.split()
        if words[1] not in mailcount:
            mailcount[words[1]]=1
        else:
            mailcount[words[1]]+=1
    largest=None
    for key in mailcount:
        if largest==None or mailcount[key]>mailcount[largest]:
            largest=key

    print(largest,' ' ,mailcount[largest])

#countEmailAddrAndFindMax()

'''
Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from (i.e., the whole email address). 
At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
'''


def countdomain():
    try:
        fname=input('please enter a file name:')
        fhand=open(fname)
    except:
        print('Can not open the file: ', fname)
        exit()
    mailcount=dict()
    for line in fhand:
        line=line.rstrip()

        if len(line)==0 or line.startswith('Author')==False:  continue
        words=line.split()

        word=words[1]
        subword=word[word.find('@')+1:]
        if subword not in mailcount:
            mailcount[subword]=1
        else:
            mailcount[subword]+=1
    print(mailcount)


#countdomain()


'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the dictionary using 
a maximum loop to find the most prolific committer.
'''


