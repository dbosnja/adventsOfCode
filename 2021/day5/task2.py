#!/bin/python3

import re
from math import gcd
from collections import defaultdict


def get_input(file_path):
    reg = re.compile(r'(\d+),(\d+)\s*->\s*(\d+),(\d+)')
    lines = []
    with open(file_path) as f:
        for line in f:
            a, b, c, d = [int(c) for c in reg.search(line.strip()).groups()]
            lines.append([(a, b), (c, d)])
    return lines


def update_point_map(line, point_map):
    (a, b), (c, d) = line
    vec_x, vec_y = c - a, d - b
    _gcd = gcd(vec_x, vec_y)
    vec_x, vec_y = vec_x // _gcd, vec_y // _gcd
    while a != c or b != d:
        point_map[a, b] += 1
        a, b = a + vec_x, b + vec_y
    point_map[c, d] += 1


def main():
    file_path = 'input.txt'
    lines = get_input(file_path)
    point_map = defaultdict(int)
    for line in lines:
        update_point_map(line, point_map)
    cnt = 0
    for occur in point_map.values():
        if occur > 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()