#!/usr/bin/python3
# Lockboxes
""" Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # Mark the first box as visited
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
