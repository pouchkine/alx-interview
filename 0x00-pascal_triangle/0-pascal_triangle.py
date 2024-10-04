#!/usr/bin/python3
'''
determine a tree of the pascal trinangle
'''


def pascal(n):
    '''
    n: height of the pascal tree
    '''
    ancien = [1]
    nouveau = ancien.copy()
    for i in range(n):
        print(nouveau)
        ancien = nouveau.copy()
        ancien.append(0)
        nouveau = ancien.copy()
        nouveau[0] = 1
        for j in range(1, len(ancien)):
            nouveau[j] = ancien[j-1] + ancien[j]
