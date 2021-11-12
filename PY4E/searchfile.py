'''
fhand=open("mbox-short.txt")
for line in fhand:
    if line.startswith("From:"):
        line=line.rstrip()
        print(line)


for line in fhand:
    line=line.rstrip()
    if line.find('@uct.ac.za')==-1:
        continue
    else:
        print(line)
'''

fname=input('please enter a file name:')
try:
    fhand=open(fname)
except:
    print("File can not be opened: ",fname)
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count+=1
print('There were ',count, 'subject lines in ',fname)
