#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin
    if total != 0:
        return -1

    return count
