
import re
def searchstr():
    fname=input('enter a file name: ')
    try:
        fhand=open(fname)
    except:
        print("Can not open file: ",fname)
        exit()
    for line in fhand:
        line=line.rstrip()
        if re.search('^From:.+@',line):
            print(line)


#searchstr()



def findAllEmailAddr():
    fname=input('enter a file name: ')
    try:
        fhand=open(fname)
    except:
        print("Can not open file: ",fname)
        exit()
    for line in fhand:
        line=line.rstrip()
        x=re.findall('\S+@\S+',line)
        if len(x)>0: 
            print(x)


#findAllEmailAddr()


def findAllEmailAddr_plus():
    fname=input('enter a file name: ')
    try:
        fhand=open(fname)
    except:
        print("Can not open file: ",fname)
        exit()
    for line in fhand:
        line=line.rstrip()
        x=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',line)
        if len(x)>0: 
            print(x)

#X-DSPAM-Confidence: 0.8475
def searchAndExtract():
    fname=input('enter a file name: ')
    try:
        fhand=open(fname)
    except:
        print("Can not open file: ",fname)
        exit()
    for line in fhand:
        line=line.rstrip()
        x=re.findall('^X-\S*: [0-9.]+',line)
        if len(x)>0: 
            print(x)


searchAndExtract()