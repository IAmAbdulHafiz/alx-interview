#!/usr/bin/python3
"""
Module for minimum operations problem.
"""

def minOperations(n):
    """
    Function minOperations
    Returns an integer
    """
    answer = 0
    neba = 2
    while n > 1:
        while n % neba == 0:
            result += neba
            n /= neba
        neba += 1
    return answer
