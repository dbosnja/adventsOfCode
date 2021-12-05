#!/bin/python3

import re
from collections import defaultdict


def get_input(file_path):
    reg = re.compile(r'(\d+),(\d+)\s*->\s*(\d+),(\d+)')
    lines = []
    with open(file_path) as f:
        for line in f:
            a, b, c, d = [int(c) for c in reg.search(line.strip()).groups()]
            lines.append([(a, b), (c, d)])
    return lines


def main():
    file_path = 'input.txt'
    lines = get_input(file_path)
    lines = [[(a, b), (c, d)] for (a, b), (c, d) in lines if a == c or b == d]
    point_map = defaultdict(int)
    for line in lines:
        (a, b), (c, d) = line
        if a == c:
            for i in range(min(b, d), max(b, d) + 1):
                point_map[a, i] += 1
        elif b == d:
            for i in range(min(a, c), max(a, c) + 1):
                point_map[i, b] += 1
    cnt = 0
    for occur in point_map.values():
        if occur > 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()