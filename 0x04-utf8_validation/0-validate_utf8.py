#!/usr/bin/python3

""" UTF-8 Validation """


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate through each integer in the data
    for byte in data:
        mask = 1 << 7

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte character or invalid leading byte
            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # All characters should have been fully parsed
    return num_bytes == 0
