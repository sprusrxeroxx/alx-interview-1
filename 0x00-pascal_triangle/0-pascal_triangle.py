"""This module solves pascal triangle using nested loops"""


def pascal_triangle(n):
    """Pascal Triangle"""
    triangle = []
    if n <= 0:
        return [[]]
    else:
        for x in range(n):
            currentRow = []
            for y in range(x + 1):
                if y == 0 or y == x:
                    currentRow.append(1)
                else:
                    prevRow = triangle[x - 1]
                    currentRow.append(prevRow[y] + prevRow[y - 1])
            triangle.append(currentRow)
        return triangle
