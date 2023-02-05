import os
import sys

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

# main area

if __name__ == '__main__':
    test = [0, 1, 2, 3, 4, 5, 6]

    print(allAttackList(test, 4))

