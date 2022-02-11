#!/usr/bin/env python3

def alist(position=0, a=None):
    a=[1,2,3]
    a.insert(position, 0)
    print(a)
    return a

if __name__ == "__main__":
    # Result of following line: [0, 1, 2, 3]
    a = aList(0)
    # 0
    print(a.index(0))
    # 1
    print(a.index(1))

    # [1, 0, 2, 3]
    a = aList(1)
    # 1
    print(a.index(0))
    # 0
    print(a.index(1))
