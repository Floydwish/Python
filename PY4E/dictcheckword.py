
'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. Then you can use the in operator as a fast way 
to check whether a string is in the dictionary.

'''


def checkword():
    try:
        fname=input("Please enter a file name:")
        fhand=open(fname)
    except:
        print('Can not open file:',fname)
        exit()
    dic=dict()
    for line in fhand:
        line=line.rstrip()
        words=line.split()
        if len(words)==0:   continue
        for word in words:
            dic[word]=''
    while(True):
        try:
            word=input('Enter a word:(enter done for quit)')
            if word=='done':
                break
            if word in dic:
                print(fname,' contains word: ',word)
            else:
                print(fname,' is not contains word: ',word)
        except:
            print('Error word input')
            continue


checkword()