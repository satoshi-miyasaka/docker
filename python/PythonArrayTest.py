import os
import sys
import itertools

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

def allAttackList2(argList, maxCount):

    # 最大数ならディープコピーしてリターン
    if maxCount == len(argList): return [[i for i in argList]]

    ret = []
    for a in itertools.product(argList, repeat = len(argList) - maxCount):
        if len(a) == len(set(a)): continue

        work = []
        for i in argList:
            if 0 == a.count(i): work.append(i)
        ret.append(work)

    return sorted(ret)

# main area

if __name__ == '__main__':
    test = list(range(7))
    print(allAttackList2(test, 7))

