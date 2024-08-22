#!/usr/bin/python3
"""Determine the fewest number of coins
"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total
    0 if total is 0 or less, -1 if total cannot be met
    """
    if total <= 0:
        return 0

    # Coins validity check
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    availableCoins = sorted(coins, reverse=True)
    changeLeft = total

    for coin in availableCoins:
        while (changeLeft % coin >= 0 and changeLeft >= coin):
            change += int(changeLeft / coin)
            changeLeft = changeLeft % coin

    change = change if changeLeft == 0 else -1

    return change
