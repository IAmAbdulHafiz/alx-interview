#!/usr/bin/python3
"""Minimum Operations
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    Args:
        n (int): The number of desired H characters.

    Returns:
        int: The number of minimal operations needed to get n H characters
    or 0 if it is impossible to achieve n.
    """
    if not isinstance(n, int):
        return 0
    opt = 0
    buf = 0
    curent = 1
    while curent < n:
        if buf == 0:
            buf = curent
            curent += buf
            opt += 2
        elif n - curent > 0 and (n - curent) % curent == 0:
            buf = curent
            curent += buf
            opt += 2
        elif buf > 0:
            curent += buf
            opt += 1
    return opt
