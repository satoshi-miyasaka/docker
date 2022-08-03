import MySQLdb

connection = MySQLdb.connect(
        host='loto',
        user='loto',
        passwd='loto',
        db='loto')

cursor = connection.cursor(MySQLdb.cursors.DictCursor)

list = [0] * 44
cursor.execute("SELECT * FROM loto6 order by number desc")
rows = cursor.fetchall()
for row in rows:
    list[row['ball_1']] += 1
    list[row['ball_2']] += 1
    list[row['ball_3']] += 1
    list[row['ball_4']] += 1
    list[row['ball_5']] += 1
    list[row['ball_6']] += 1
    list[row['bonus']] += 1

for l in list:
    print(l)


connection.commit()

connection.close()

