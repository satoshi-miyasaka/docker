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
	'bonus' : 9
}

loto7_jnb_cols = {
	'ball_1' : 3,
	'ball_2' : 4,
	'ball_3' : 5,
	'ball_4' : 6,
	'ball_5' : 7,
	'ball_6' : 8,
	'ball_7' : 9,
	'bonus1' : 10,
	'bonus2' : 11
}

def csv_input(connection, input_file, column_dict, table_name):
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
			iv = []
			uv = []
			for key in column_dict:
				iv.append('%s')
				uv.append(key + ' = %s')
				orec.append(str(int(row[column_dict[key]])))

			cursor.execute("SELECT count(1) FROM " + table_name + " where number = '" + str(number) + "'")
			rows = cursor.fetchall()


			sql = ''
			if 0 == rows[0][0]:
				orec.insert(0, str(int(number)))
				iv.append('%s')
				sql = "INSERT " + table_name + " values(" + ", ".join(iv) + ")"
			else:
				orec.append(str(int(number)))
				sql = "UPDATE " + table_name + " set " + ", ".join(uv) + " where number = %s"
			cursor.execute(sql, orec)

connection = MySQLdb.connect(
        host='loto',
        user='loto',
        passwd='loto',
        db='loto')

csv_input(connection, '/root/loto6jnb.csv', loto6_jnb_cols, 'loto6')
# csv_input(connection, '/root/loto7jnb.csv', loto7_jnb_cols, 'loto7')

connection.commit()

connection.close()
