#!/usr/bin/python3
"""This module contains solution to lockboxes trivial question"""

def canUnlockAll(boxes):
    """A function thatdetermines if all the boxes can be opened."""
    boxLen = len(boxes)
    found_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= boxLen or boxIdx < 0:
            continue
        if boxIdx not in found_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            found_boxes.add(boxIdx)
    return boxLen == len(found_boxes)
