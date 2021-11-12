#1.create a database file
#1.using sqlite3

import sqlite3

def createdb():
    conn=sqlite3.connect('music.sqlite')
    cur=conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Tracks')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
    conn.close()

#createdb()

def dbinsert():
    conn=sqlite3.connect('music.sqlite')
    cur=conn.cursor()

    cur.execute('INSERT INTO Tracks (title,plays) VALUES(?,?)',('Thunder',20))
    cur.execute('INSERT INTO Tracks (title,plays) VALUES(?,?)',('my way',15))
    conn.commit()

    print('print Tracks')
    cur.execute('SELECT title,plays FROM Tracks')
    for row in cur:
        print(row)

    cur.execute('DELETE FROM Tracks where plays<100')
    conn.commit()

    cur.close()


#dbinsert()


def readsqlite():
    fname=input('Please enter a sqlite name: ')
    #table=input('Please enter the table name: ')
    conn=sqlite3.connect('friends.sqlite')
    cur=conn.cursor()

    cur.execute('SELECT * FROM Follows JOIN People ON Follows.from_id = People.id WHERE People.id =1')
    conn.commit()

    for row in cur:
        print(row)

readsqlite()