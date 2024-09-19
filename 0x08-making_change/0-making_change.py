#!/usr/bin/env python3
"""
ALX INTERVIEW QUESTION
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    If the total cannot be met by any combination of coins, return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
