fhand=open('mbox.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    s=line.split()
    print(s[2])