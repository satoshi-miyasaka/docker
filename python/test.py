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

if (7 > len(list)):
    list2 = []
    cursor.execute("SELECT ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, bonus FROM loto6 order by number desc")
    rows = cursor.fetchall()
    for row in rows:
        list2.append(row[0])
        list2.append(row[1])
        list2.append(row[2])
        list2.append(row[3])
        list2.append(row[4])
        list2.append(row[5])
        list2.append(row[6])
    
        max = 0
        for l in list2:
            if max < list2.count(l):
                max = list2.count(l)

        list3 = []
        for l in list2:
            if (max == list2.count(l)):
                if (0 == list3.count(l)):
                    list3.append(l) 

        if (7 == (len(list) + len(list3))):
            list += list3
            break
list.sort()
print(list)

connection.commit()

connection.close()

