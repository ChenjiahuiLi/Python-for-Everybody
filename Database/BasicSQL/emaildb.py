import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# 
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    print email
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, )) # use ? to avoid SQL injection
    # row = cur.fetchone() 
    # fetch one: brings us one row into memory and gives to us as a list, 
    # and then sub 0 which is the count field in the database
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email,))
    except:
        cur.execute('''INSERT INTO Counts(email,count) VALUES (?,1)''', (email,))

    #if row is None:
    #    cur.execute('''INSERT INTO Counts (email, count) VALUES ( ?, 1 )''', ( email, ) )
    # else : 
    #    cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', (email, ))

    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    # conn.commit()

conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# the top10 email senders

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

