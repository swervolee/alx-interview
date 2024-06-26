#!/usr/bin/python3
"""
ALX INTERVIEW QUESTION
"""


def canUnlockAll(boxes):
    """
    ALX INTERVIEW QUESTION
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]

    while keys:
        new_key = keys.pop()
        if new_key < n and not opened[new_key]:
            opened[new_key] = True
            keys.extend(boxes[new_key])
    return all(opened)
