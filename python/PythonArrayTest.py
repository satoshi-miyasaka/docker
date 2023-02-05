import os
import sys

# function area

def allAttackList(list, max):
    work = []

    # 最大数ならディープコピーしてリターン
    if max == len(list):
        for i in list: work.append(i)
        return [work]

    ret = []
    # 配列をディープコピーしてから後ろから順に１文字削除
    for i in sorted(list, reverse=True):
        temp = []
        for j in list: temp.append(j)
        temp.remove(i)
        # 再帰で呼び出し、二次元配列を返してもらう
        work += allAttackList(temp, max)

    # 重複している配列を削除する
    for l in work:
        if 0 == ret.count(l): ret.append(l)

    return ret

# main area

if __name__ == '__main__':
    test = [0, 1, 2, 3, 4, 5, 6]

    print(allAttackList(test, 4))

