#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    file_size, count_me = 0, 0
    s_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    sts = {y: 0 for y in s_codes}

    def print_sts(sts: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for y, z in sorted(sts.items()):
            if z:
                print("{}: {}".format(y, z))

    try:
        for line in sys.stdin:
            count_me += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in sts:
                    sts[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            if count_me % 10 == 0:
                print_sts(sts, file_size)
        print_sts(sts, file_size)
    except yeyboardInterrupt:
        print_sts(sts, file_size)
        raise
