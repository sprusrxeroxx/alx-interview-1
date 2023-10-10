#!/usr/bin/python3
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
    #  Assume the file contain 1 alphabet (H)
    fileText = 1
    #  Assume nothing has been copied to the clipboard yet
    copyText = 0
    #  No operation has been done yet
    countOperation = 0

    while fileText < n:
        #  Copy All when the length of text is divisible by n
        if n % fileText == 0:
            copyText = fileText
            countOperation += 1

        #  Paste at all time. Action 2
        fileText += copyText
        countOperation += 1
    return countOperation
