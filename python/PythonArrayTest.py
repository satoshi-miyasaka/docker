import os
import sys
import itertools

# function area

def allAttackList(list, max):
    work = []

    # $B:GBg?t$J$i%G%#!<%W%3%T!<$7$F%j%?!<%s(B
    if max == len(list):
        for i in list: work.append(i)
        return [work]

    ret = []
    # $BG[Ns$r%G%#!<%W%3%T!<$7$F$+$i8e$m$+$i=g$K#1J8;z:o=|(B
    for i in sorted(list, reverse=True):
        temp = []
        for j in list: temp.append(j)
        temp.remove(i)
        # $B:F5"$G8F$S=P$7!"Fs<!85G[Ns$rJV$7$F$b$i$&(B
        work += allAttackList(temp, max)

    # $B=EJ#$7$F$$$kG[Ns$r:o=|$9$k(B
    for l in work:
        if 0 == ret.count(l): ret.append(l)

    return ret

def allAttackList2(argList, maxCount):

    # $B:GBg?t$J$i%G%#!<%W%3%T!<$7$F%j%?!<%s(B
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

