#!/bin/python3

import MySQLdb

connection = MySQLdb.connect(
        host='loto',
        user='loto',
        passwd='loto',
        db='loto')

cursor = connection.cursor()

list = {}
for i in range(1, 44):
	list[i] = 0

cursor.execute("SELECT ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, bonus FROM loto6")
rows = cursor.fetchall()

for row in rows:
	for col in row:
		list[col] += 1

list2 = sorted(list.items(), key=lambda x:x[1])

temp = []
for i in range(7):
    temp.append(list2[i][0])
temp.sort()
print(temp)

connection.commit()

connection.close()

