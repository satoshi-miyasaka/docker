import MySQLdb

connection = MySQLdb.connect(
        host='loto',
        user='loto',
        passwd='loto',
        db='loto')

cursor = connection.cursor()

cursor.execute("SELECT * FROM loto6")
rows = cursor.fetchall()
for row in rows:
    print ( row ) 

connection.commit()

connection.close()

