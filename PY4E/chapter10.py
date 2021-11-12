'''
calculate a text file's words frequency
'''
import string

fname=input('Please enter a text file name: ')
fhand=open(fname)

#get all words and store in dict
counts=dict()
for line in fhand:
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
            
#sort the list by value and output top 10
lst=list()

for key,val in list(counts.items()):
    lst.append((val,key))

lst.sort(reverse=True)

for key,val in lst[:10]:
    print(key,val)


