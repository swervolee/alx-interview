#!/usr/bin/python3
"""
UTF-8 validation
"""

def validUTF8(data):
    """
    Validating utf8
    """
    i = 0
    n = len(data)

    while i < n:
        byte = data[i]

        if byte < 0x80:
            i += 1
        elif 0xC2 <= byte <= 0xDF:
            # 2-byte sequence
            if i + 1 >= n or not (0x80 <= data[i + 1] <= 0xBF):
                return False
            i += 2
        elif 0xE0 <= byte <= 0xEF:
            if i + 2 >= n or not (0x80 <= data[i + 1] <= 0xBF
                                  ) or not (
                                      0x80 <= data[i + 2] <= 0xBF):
                return False
            i += 3
        elif 0xF0 <= byte <= 0xF4:
            if i + 3 >= n or not (0x80 <= data[i + 1] <= 0xBF
                                  ) or not (0x80 <= data[
                                      i + 2] <= 0xBF
                                            ) or not (
                                                0x80 <= data[
                                                    i + 3] <= 0xBF):
                return False
            i += 4
        else:
            return False
    return True
