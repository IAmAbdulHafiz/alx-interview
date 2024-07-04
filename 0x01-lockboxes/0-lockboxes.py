#!/usr/bin/python3
"""
Lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for jb in range(1, len(boxes) - 1):
        boxes_chkd = False
        for indx in range(len(boxes)):
            boxes_chkd = jb in boxes[indx] and jb != indx
            if boxes_chkd:
                break
        if boxes_chkd is False:
            return boxes_chkd
    return True
