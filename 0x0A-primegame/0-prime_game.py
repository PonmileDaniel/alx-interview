#!/usr/bin/python3
"""
Define isWinner function, a soln to the prime
"""


def sieve_of_eratosthenes(max_n):
    """Precomputes prime numbers and their cumulative count up to max_n."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    return prime_count


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    prime_count = sieve_of_eratosthenes(max_n)
    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        if prime_count[n] % 2 == 1:
            wins['Maria'] += 1
        else:
            wins['Ben'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Ben'] > wins['Maria']:
        return 'Ben'
    else:
        return None
