#!/usr/bin/python3
""" prime game between ben && Maria """
""" x is number of rounds """
""" every round x have a != n"""
""" nums array of n """
""" n && x < 10000 """
""" Example:
    x = 3, nums = [4, 5, 1]
First round: 4
    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose
"""


def isWinner(x, nums):
    """condition for x && n"""
    if x < 1 or x > 10000 or len(nums) > 10000:
        return None
    """ start with no action all players """
    marias_wins, bens_wins = 0, 0
    """ Generate primes with a limit of the maximum number in nums"""
    n = max(nums)
    primes = []
    for _ in range(1, n + 1):
        primes.append(True)
    primes[0] = False
    for i, prime in enumerate(primes, 1):
        if i == 1 or not prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    """Count primes < each number in nums for X round """
    for num in nums:
        primes_count = sum(primes[:num])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return "Maria"
    else:
        return "Ben"
