import os
import sys

# function area

def allAttackList(args):
    ret = []
    lastNumber = args.pop()
    ret.append(args)

    for i in range(len(args)):
        temp = []
        for j in args:
            if i == args.index(j):
                temp.append(lastNumber)
            else:
                temp.append(j)

        ret.append(sorted(temp))

    return sorted(ret)

def setList(baseList, addList):
    if 0 == baseList.count(addList):
        baseList.append(addList)

# main area

if __name__ == '__main__':
    test = [0, 1, 2, 3]
    ret = []

    for work in allAttackList(test):
        for temp in allAttackList(work):
            setList(ret, temp)

    print(len(ret))
    print(sorted(ret))

