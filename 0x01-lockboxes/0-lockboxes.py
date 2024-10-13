#!/usr/bin/python3

"""
check if i can unloke the boxes
"""


def canUnlockAll(boxes):
    """
    boxes are the boxes contening keys
    """
    n = len(boxes)
    keys_boxes = set(boxes[0] + [0])
    key_boxes_before = {0}
    index_portes_ouverte = {0}
    while (key_boxes_before != keys_boxes):
        key_boxes_before = keys_boxes.copy()
        for i in range(1, n):
            if i in keys_boxes:
                index_portes_ouverte.add(i)
                keys_boxes.update(boxes[i])
    if len(index_portes_ouverte) == n:
        return True
    else:
        return False
