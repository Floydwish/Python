
fname=input('please enter a file name: ')
try:
    fhand=open(fname)
except:
    print('File can not opened ',fname)
    exit()
for line in fhand:
    print(line.upper().strip())