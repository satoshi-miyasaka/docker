import os
import sys

# function area

def allAttackList(list, max):
    work = []
    ret = []

    if max == len(list):
        for i in list: work.append(i)
        ret.append(work)
        return ret

    for i in sorted(list, reverse=True):
        temp = []
        for j in list: temp.append(j)
        temp.remove(i)
        work += allAttackList(temp, max)

    # 重複削除
    for l in work:
        if 0 == ret.count(l):
            ret.append(l)

    return ret

# main area

if __name__ == '__main__':
    test = [0, 1, 2, 3, 4, 5, 6]

    print(allAttackList(test, 4))

