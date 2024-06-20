#!/usr/bin/python3
"""
LOG PARSING
"""
import sys
from datetime import datetime
from typing import List, Union
import select


def check_format(line: str) -> Union[List[int], bool]:
    """
    Checks if the line has the format
    <IP Address> - [<date>] "GET /projects/260
    HTTP/1.1" <status code> <file size>
    """
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        args = line.split(" - ")
        ip = args[0]

        if ip.count(".") != 3:
            return False

        format_string = "%Y-%m-%d %H:%M:%S.%f"

        args = args[1].split("] ")
        date_string = args[0][1:]

        try:
            real_date = datetime.strptime(date_string, format_string)
        except Exception:
            return False

        args = args[1].split('" ')

        request = args[0].strip('"')
        if request != "GET /projects/260 HTTP/1.1":
            return False

        code, file_size = int(args[1].split()[0]), int(args[1].split()[1])

        if code not in status_codes:
            return False

        return [code, file_size]
    except Exception:
        return False


def print_info(file_size, codes):
    """
    prints info
    """
    response_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    print(f"File size: {file_size}")
    for code in sorted(set(codes)):
        if code in response_codes:
            print(f"{code}: {codes.count(code)}")


if __name__ == "__main__":
    file_size = 0
    codes = []
    counter = 0

    while True:
        try:
            for line in sys.stdin:
                if counter == 10:
                    print_info(file_size, codes)
                    counter = 0
                result = check_format(line)
                if result:
                    codes.append(result[0])
                    file_size += result[1]
                counter += 1
        except KeyboardInterrupt:
            print_info(file_size, codes)
            counter = 0
            continue
