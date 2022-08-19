#!/bin/python3
# 全体から最近出現率の低いボールをｎ個
# 最近出現率が低いボールをｍ個
# 選ぶボール数がｌ個として
# l - (n + m) = o で計算し、
# 最近出現率の高いボールをｏ個選ぶ
# ｎとｍのボールに重複がある場合、重複したボール数分ｏが増える

import MySQLdb
import csv

n = 2
m = 5
l = 7
o = 0

loto6_jnb_cols = {
	'ball_1' : 3,
	'ball_2' : 4,
	'ball_3' : 5,
	'ball_4' : 6,
	'ball_5' : 7,
	'ball_6' : 8,
	'ball_b' : 9
}

loto7_jnb_cols = {
	'ball_1' : 3,
	'ball_2' : 4,
	'ball_3' : 5,
	'ball_4' : 6,
	'ball_5' : 7,
	'ball_6' : 8,
	'ball_7' : 9,
	'ball_b1': 10,
	'ball_b2': 11
}

def csv_input(connection, input_file, column_dict):
	cursor = connection.cursor()
	c = 0
	with open(input_file, encoding='sjis') as i:
		reader = csv.reader(i)
		for row in reader:
			c += 1
			orec = []
			if 1 == c:
				continue

			number = row[0].replace('第', '').replace('回', '')
			for key in column_dict:
				orec.append(str(int(row[column_dict[key]])))

			cursor.execute("SELECT count(1) FROM loto6 where number = '" + str(number) + "'")
			rows = cursor.fetchall()

			if 0 == rows[0][0]:
				orec.insert(0, str(int(number)))
				cursor.execute("INSERT loto6 values(%s, %s, %s, %s, %s, %s, %s)", orec)
			else:
				orec.append(str(int(number)))
				cursor.execute("update loto6 set ball_1 = %s, ball_2 = %s, ball_3 = %s, ball_4 = %s, ball_5 = %s, ball_6 = %s, bonus = %s where number = %s", orec)

connection = MySQLdb.connect(
        host='loto',
        user='loto',
        passwd='loto',
        db='loto')


csv_input(connection, '/root/loto6jnb.csv', loto6_jnb_cols)
#csv_input(connection, 'loto7jnb.csv', loto7_jnb_cols)

connection.commit()

connection.close()
