#!/usr/bin/python3

""" Utf-8 validation"""


def validUTF8(data):
    num_bytes = 0

    check1 = 1 << 7
    check2 = 1 << 6

    for byte in data:
        check1 = 1 << 7

        if num_bytes == 0:
            while check1 & byte:
                num_bytes += 1
                check1 >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            return False
        num_bytes -= 1

    return num_bytes == 0
