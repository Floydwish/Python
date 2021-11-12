import string

def countword():
    try:
        fname=input("Please enter a file name:")
        fhand=open(fname)
    except:
        print('Can not open file:',fname)
        exit()
    counts=dict()
    for line in fhand:
        line=line.rstrip()
        line=line.translate(line.maketrans('','',string.punctuation))
        line=line.lower()
        words=line.split()
        if len(words)==0:   continue
        for word in words:
            if word not in counts:
                counts[word]=1
            else:
                counts[word]+=1
    print(counts)

countword()