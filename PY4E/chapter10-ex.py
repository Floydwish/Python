'''
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and 
pull out the addresses from the line. Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) 
tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''
def parseText():
    #1.获取文件名
    fname=input('Please enter a text file name: ')

    #2.读取文件
    try:
        fhand=open(fname)
    except:
        print('Open file failed: ',fname)
        exit()

    #3.处理并提取信息
    counts=dict()
    for line in fhand:
        line=line.rstrip()
        if len(line)==0 or line.startswith('From')==False:
            continue
        words=line.split()
        if len(words)<3:
            continue
        word=words[1]
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

    #4.排序
    lst=list()
    for key,val in list(counts.items()):
        lst.append((val,key))
    lst.sort(reverse=True)

    #5.输出结果
    print(lst[0])


#parseText()



'''
Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
 You can pull the hour from the “From” line by finding the time string and then splitting that 
 string into parts using the colon character. Once you have accumulated the counts for each hour, 
 print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

'''
def emailTimeCount():
    fname=input('please enter a file name: ')
    try:
        fhand=open(fname)
    except:
        print('Open file failed: ',fname)
        exit()

    #提取信息
    counts=dict()
    for line in fhand:
        line=line.rstrip()
        if len(line)==0 or line.startswith('From')==False:
            continue
        words=line.split()
        if len(words)<5:    continue
        word=words[5]
        index=word.find(':')
        word=word[:index]

        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

    #排序
    lst=list()
    for key,val in list(counts.items()):
        lst.append((key,val))
    lst.sort(reverse=False)

    #输出结果
    for key,val in lst:
        print(key,val)



#emailTimeCount()





'''
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
Your program should convert all the input to lower case and only count the letters a-z. 
Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
Find text samples from several different languages and see how letter frequency varies between languages. 
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

'''

import string

def calTextLetters():
    fname=input('please enter a file name: ')
    try:
        fhand=open(fname)
    except:
        print('Open file failed: ',fname)
        exit()

    #提取数据
    counts=dict()
    for line in fhand:
        if len(line)==0:    continue
        line=line.translate(str.maketrans('','',string.punctuation))
        line=line.translate(str.maketrans('','',string.digits))
        line=line.translate(str.maketrans('','',string.whitespace))
        line=line.lower()
        words=line.split()
        for word in words:
            if len(word)==0:    continue
            for letter in word:
                if letter not in counts:
                    counts[letter]=1
                else:
                    counts[letter]+=1
    #排序
    lst=list()
    for key,val in list(counts.items()):
        lst.append((val,key))
    lst.sort(reverse=True)

    #输出结果
    for key,val in lst:
        print(key,val)


calTextLetters()



fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhand=open(fname)
except:
    print('Open file failed: ',fname)
    exit()

#提取信息
counts=dict()
for line in fhand:
    line=line.rstrip()
    if len(line)==0 or line.startswith('From')==False:
        continue
    words=line.split()
    if len(words)<5:    continue
    word=words[5]
    index=word.find(':')
    word=word[:index]

    if word not in counts:
        counts[word]=1
    else:
        counts[word]+=1

#排序
lst=list()
for key,val in list(counts.items()):
    lst.append((key,val))
lst.sort(reverse=False)

#输出结果
for key,val in lst:
    print(key,val)


