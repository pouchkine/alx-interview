#!/usr/bin/python3
"""make change functions
"""


def makeChange(coins, total):
    """fonction processing
    """
    min_coin = 0
    coins.sort()
    coins.reverse()
    for coin in coins:
        min_coin = min_coin + total // coin
        total = total % coin
        if total == 0:
            return min_coin
    if total > 0:
        return -1
