#!/usr/bin/python3
"""This module contain the minOperation function"""


def minOperations(n: int) -> int:
    """Calculate the fewest number of operation"""
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
