import os
import sys
import itertools

# function area

def makeBoxList(argList, maxCount):
    ret = []
    for a in itertools.product(argList, repeat = len(argList) - maxCount):
        if len(a) != len(set(a)) or list(a) != sorted(a): continue
        ret.append([i for i in argList if 0 == a.count(i)])
    return sorted(ret)

# main area

if __name__ == '__main__':
    test = list(range(7))
    print(makeBoxList(test, 7))
