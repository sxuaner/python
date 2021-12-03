#!/usr/bin/env python3

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

if __name__=="__main__": 
    print(f(1))
    print(f(2))
    print(f(3))
