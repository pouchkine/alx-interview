#!/usr/bin/python3
'''
determine a tree of the pascal trinangle
'''


def pascal_triangle(n):
    '''
    n: height of the pascal tree
    '''
    if n <= 0:
        return []
    pas = []
    ancien = [1]
    nouveau = ancien.copy()
    for i in range(n):
        pas.append(nouveau)
        ancien = nouveau.copy()
        ancien.append(0)
        nouveau = ancien.copy()
        nouveau[0] = 1
        for j in range(1, len(ancien)):
            nouveau[j] = ancien[j-1] + ancien[j]
    return pas
