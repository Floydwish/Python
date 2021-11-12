'''
Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized database with
this structure

1.连接数据库
2.清除已有的表
3.创建表用于存储music数据
4.从xml文件中解析出数据
5.将数据按照表格存储
6.查询测试


CREATE TABLE Artist (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);
CREATE TABLE Genre (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);
CREATE TABLE Album (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
artist_id INTEGER,
title TEXT UNIQUE
);
CREATE TABLE Track (
id INTEGER NOT NULL PRIMARY KEY
AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
album_id INTEGER,
genre_id INTEGER,
len INTEGER, rating INTEGER, count INTEGER
);

'''

import sqlite3
import xml.etree.ElementTree as ET


#1.连接数据库
conn = sqlite3.connect('musicdb.sqlite')
cur = conn.cursor()

#2.清除已有的表
cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')


#3.创建表用于存储music数据
cur.execute('CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Genre  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Album  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE)')
cur.execute('CREATE TABLE Track  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER,len INTEGER, rating INTEGER, count INTEGER)')

#4.从xml文件中解析出数据
#4.1查找子标签文本接口
def lookup(d,key):
    found = False
    for child in d:
        if found==True: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

#4.2解析文件提取数据
fname = input('Enter a file name: ')
if len(fname)<1: fname='Library.xml'

try:
    stuff = ET.parse(fname)
except:
    print('parse file failed: ',fname)
    exit()
results = stuff.findall('dict/dict/dict')
print('Dict count:',len(results))

for entry in results:
    try:
        if (lookup(entry,'Track ID') is None): continue
        name = lookup(entry,'Name')
        artist = lookup(entry,'Artist')
        album = lookup(entry,'Album')
        count = lookup(entry,'Play_Count')
        rating = lookup(entry,'Rating')
        length = lookup(entry,'Total Time')
        genre = lookup(entry,'Genre')

        if name is None or artist is None or album is None:
            continue
        #print(name, artist, album, count, rating, length)

        #4.3.将数据按照表格存储
        #Artist table
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
        artist_id = cur.fetchone()[0]
        #print(artist,artist_id)

        #Genre table
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
        genre_id = cur.fetchone()[0]
        #print(genre,genre_id)

        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES(?,?)',(album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?,?,?,?,?,?)''',
        (name, album_id, genre_id, length, rating, count))
    except:
        print('except:',genre,genre_id)
        continue
conn.commit()

#5.查询测试
'''
SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3
'''

