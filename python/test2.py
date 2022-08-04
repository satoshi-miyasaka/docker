#!/bin/python3
# 最近出現していないボールを７つ選ぶ
# ７個以下より少なくなってしまったら、最近よく出ている数字で残りを補完する

import MySQLdb

connection = MySQLdb.connect(
        host='loto',
        user='loto',
        passwd='loto',
        db='loto')

# cursor = connection.cursor(MySQLdb.cursors.DictCursor)
cursor = connection.cursor()

# 最初にリストに全ボールを入れて初期化
list = []
for ball in range(1, 44):
    list.append(ball)

# 新しい順に取得
# cursor.execute("SELECT * FROM loto6 order by number desc")
cursor.execute("SELECT ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, bonus FROM loto6 order by number desc")
rows = cursor.fetchall()

# リストから出現したボールを削除
for row in rows:
    for col in row:
        if (0 < list.count(col)):
            list.remove(col)
    # 残ったボールが７個以下ならループを抜ける
    # カラムの処理中に７個以下になっても抜けてはいけない
    if (7 >= len(list)):
        break

print(list)

connection.commit()

connection.close()

