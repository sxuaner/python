#!/usr/bin/env python3
import builtins

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

firstList=[1,2,3,4]

if __name__=="__main__":
    transposed=[[row[i] for row in matrix] for i in range(4)]
    print(transposed)
    original = [[row[i]for i in range(4)] for row in matrix]
    print(original)

    '''
    transposed=[[row[i] for row in matrix] for i in range(4)]
    is equvalent to: 
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    '''
    # zip() is a builtin method. checkout all builtin methods(available in __main__??)
    print(dir(builtins))
    
    transposedUsingZip=list(zip(*matrix))
    print(transposedUsingZip)

    # [ ([1, 2, 3, 4],), 
    #   ([5, 6, 7, 8],), 
    #   ([9, 10, 11, 12],) ]
    zippedMatrix = list(zip(matrix))
    print(" zipperMatrix: ", zippedMatrix)

    # [(1,), (2,), (3,), (4,)]
    zippedFirstList=  list(zip(firstList))
    print(zippedFirstList)
