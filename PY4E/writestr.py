
fname=input("please enter file name: ")
try:
    fhand=open(fname,'w')
except:
    print('File can not opened: ',fname)
    exit()

s='writting something for test\n'
n=fhand.write(s)
print("written ",n, "charcters in ",fname)
fhand.close()