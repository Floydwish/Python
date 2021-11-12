import sqlite3

#1.连接数据库
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

#2.如果表已经存在，删除
cur.execute('DROP TABLE IF EXISTS Counts')

#3.每次重新创建表
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#4.获取需要计算的文件
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'   #默认文件
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    orgstr = email[email.find('@')+1:]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgstr,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (orgstr,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (orgstr,))
conn.commit()

# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
