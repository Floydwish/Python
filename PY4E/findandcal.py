
fname=input('please enter a file name: ')

try:
    fhand=open(fname)
except:

    print(fname.upper(),'TO YOU, you have been punk\'d')
    exit()

try:
    count=0
    total=0.0
    for line in fhand:
        if  line.startswith('X-DSPAM-Confidence:'):
            pos=line.find(':')
            s=line[pos+1:]
            s=s.strip()
            total+=float(s)
            count+=1
    print('Average spam confidence: ',total/count)
except:
    print('read file failed')
    exit()


