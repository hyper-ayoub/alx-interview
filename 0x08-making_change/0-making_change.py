#!/usr/bin/python3

""" coins problem """


def makeChange(coins, total):
    # If total is zero, no coins are needed
    if total == 0:
        return 0
    # using bottom up

    but = [total + 1] * (total + 1)
    # start with fisrt posiition
    but[0] = 0

    for i in range(1, total + 1):
        for j in coins:
            if j <= i:
                but[i] = min(but[i], 1 + but[i - j])

    # return statement
    return but[total] if but[total] != total + 1 else -1
