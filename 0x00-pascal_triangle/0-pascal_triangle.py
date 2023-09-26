"""This module solves pascal triangle using nested loops"""


def pascal_triangle(n):
    """Pascal Triangle"""
    triangle = []
    for x in range(n + 1):
        currentRow = []
        for y in range(x + 1):
            if y == 0 or y == x:
                currentRow.append(1)
            else:
                currentRow.append(triangle[x - 1][y] + triangle[x - 1][y -1])
        triangle.append(currentRow)
    return triangle