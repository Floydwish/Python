import json
import sqlite3


#1.连接数据库
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#2.删除已有表格，重新创建表格
# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

#3.读入文件，或使用默认文件
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#4.将文件数据加载到json对象
str_data = open(fname).read()
json_data = json.loads(str_data)


#5.从json中取出数据
#6.插入到数据库
for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

conn.commit()  



'''
test:

SELECT User.name,Course.title, Member.role FROM User JOIN Member JOIN Course ON 
User.id = Member.user_id AND Member.course_id = Course.id ORDER BY 
User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course ON 
User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X LIMIT 1


'''
