import pymysql

con = pymysql.connect('remotemysql.com', '1XMpLk3PTn',
    'j3Ukgu30qC', '1XMpLk3PTn')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Tb_IMSbot")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
