#!/bin/python3
# 全体から最近出現率の低いボールをｎ個
# 最近出現率が低いボールをｍ個
# 選ぶボール数がｌ個として
# l - (n + m) = o で計算し、
# 最近出現率の高いボールをｏ個選ぶ
# ｎとｍのボールに重複がある場合、重複したボール数分ｏが増える

import MySQLdb

n = 2
m = 4
l = 6
o = 0

connection = MySQLdb.connect(
	host='loto',
	user='loto',
	passwd='loto',
	db='loto')

# cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor = connection.cursor()

# 全体から出現率の少ないｎ個を選ぶ
dict = {}
for i in range(1, 44):
	dict[i] = 0

cursor.execute("SELECT ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, bonus FROM loto6")
rows = cursor.fetchall()

for row in rows:
	for col in row:
		dict[col] += 1

sort_dict = sorted(dict.items(), key=lambda x:x[1])

marge_list = []
for i in range(n):
	marge_list.append(sort_dict[i][0])

# 最初にリストに全ボールを入れて初期化
list = []
dict = {}
for ball in range(1, 44):
	list.append(ball)
	dict[ball] = 0

# 新しい順に取得
# cursor.execute("SELECT * FROM loto6 order by number desc")
cursor.execute("SELECT ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, bonus FROM loto6 order by number desc")
rows = cursor.fetchall()

# リストから出現したボールを削除
# 出現率の高いボールを選ぶため、辞書にボール数も補完する
limit = 7
flg = 1
for row in rows:
	limit -= 1
	if 0 >= limit and 0 == flg:
		break

	for col in row:
		dict[col] += 1
		if (1 == flg and 0 < list.count(col)):
			list.remove(col)

	if (m >= len(list)):
		flg = 0

for i in list:
	if (0 == marge_list.count(i)):
		marge_list.append(i)

# 最近出現率の高いボールを選ぶ
sort_dict = sorted(dict.items(), reverse=True, key=lambda x:x[1])

for o in sort_dict:
	if l <= len(marge_list):
		break

	if 0 == marge_list.count(o[0]):
		marge_list.append(o[0])

marge_list.sort()
print(marge_list)

connection.commit()

connection.close()

