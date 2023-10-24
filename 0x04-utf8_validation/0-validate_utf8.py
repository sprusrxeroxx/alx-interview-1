#!/usr/bin/python3
"""This module contains function that checks
if characters are utf-8 encoding or not"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    if not data:
        return False

    for num in data:
        if not isinstance(int, num) or num < 0:
            return False

        # get the 8 least significant bits
        num = num & 0xFF

        # if num is 1-byte (8-bits)
        if num <= 0x7F:
            continue
        # if num is 2-bytes (16-bits)
        elif num <= 0x7FF:
            if not (0b11000000 <= num <= 0b11011111):
                return False
        # if num is 3-bytes(24-bits)
        elif num <= 0xFFFF:
            if not (0b11100000 <= num <= 0b11101111):
                return False
        # if num is 4-bytes (32-bits)
        elif num <= 0x10FFFF:
            if not (0b11110000 <= num <= 0b11110100):
                return False

    return True
