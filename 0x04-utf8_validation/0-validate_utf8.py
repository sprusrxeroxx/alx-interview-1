#!/usr/bin/python3
"""This module contains function that checks
if characters are utf-8 encoding or not"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determine if a given datda set represents a valid UTF-8 encoding"""
    binary_sequence = ['10', '110', '1110', '11110']

    if not data or any(not isinstance(int, x) for x in data):
        return False

    first_byte = bin(data[0])[2:]
    """If there is only one element in a list"""
    if len(data) == 1:
        if len(first_byte) <= 8:
            if any(first_byte.startswith(i) for i in binary_sequence):
                return True
        return False

    """Convert list emements to binary and check their length"""
    for i in data:
        if len(bin(i)[2:]) > 8:
            return False
        if any(bin(i)[2:].startswith(j) for j in binary_sequence):
            continue
        else:
            return False

    return True
