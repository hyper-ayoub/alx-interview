#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """ function for min Operation"""
    operations = 0
    minOperations = 2  # Start from 2 instead of 0
    while n > 1:
        while n % minOperations == 0:
            operations += minOperations
            n /= minOperations
        minOperations += 1
    return operations  # Return operations instead of minOperations
