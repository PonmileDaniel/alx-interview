#!/usr/bin/python3

"""
    Annontation for Variable
    """


def canUnlockAll(boxes):
    """Total number of boxes"""
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()

        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n

