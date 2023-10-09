#!/usr/bin/env python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
"""


def minOperations(n: int) -> int:
    """This function counts the number of operations i.e copy and paste,
    to achieve a length of a text in a file that initially contains one
    alphabet 'H'"""
    if n <= 0:
        return 0
    """Initial content of the file"""
    fileText = 1
    """Content in the clipboard"""
    copyText = 0
    """No operation done yet"""
    minOperation = 0
    """displayOpe = [] To print out the operation, remove the docstring"""

    """while the file content is still < actual length"""
    while fileText < n:
        """The copyAll operation. Increase the minOperation for copy
        operation """
        if n % fileText == 0:
            copyText = fileText
            minOperation += 1
        """displayOpe.append('Copy All') To print out the operation, remove
        the doctring"""

        """The paste Operation. Increase the minOperation for paste
        operation"""
        fileText += copyText
        minOperation += 1
        """displayOpe.append('Paste') To print out the operation,
        uncomment this print(displayOpe) To print out the operation,
        uncomment this"""
    return minOperation
