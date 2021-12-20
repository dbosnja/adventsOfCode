#!/usr/bin/python3

import re
from math import atan2
from itertools import product


def get_input(file_path):
    reg = re.compile(r'x=(-?\d+)\.\.(-?\d+),\s*y=(-?\d+)\.\.(-?\d+)')
    with open(file_path) as f:
        line = f.readline().strip()
        return [int(c) for c in reg.findall(line)[0]]


def get_cadidates():
    domain = product(range(1000), repeat=2)
    for i, j in sorted(domain, key=lambda X: atan2(X[1], X[0]), reverse=True):
        if i == j == 0:
            continue
        yield i, j


def get_trajectory(vec_x, vec_y, borders):
    _, _, y_min, _ = borders
    tmp_x, tmp_y = 0, 0
    trajectory = []
    while True:
        tmp_x, tmp_y = vec_x + tmp_x, tmp_y + vec_y
        if tmp_y < y_min:
            break
        trajectory.append((tmp_x, tmp_y))
        if vec_x > 0:
            vec_x -= 1
        elif vec_x < 0:
            vec_x += 1
        vec_y -= 1
    return trajectory


def is_on_target(trajectory, borders):
    x_min, x_max, y_min, y_max = borders
    if any(x_min <= x <= x_max and y_min <= y <= y_max for x, y in trajectory):
        return True
    return False


def main():
    file_path = 'input.txt'
    borders = get_input(file_path)
    for vec_x, vec_y in get_cadidates():
        trajectory = get_trajectory(vec_x, vec_y, borders)
        if is_on_target(trajectory, borders):
            break
    print(max(y for _, y in trajectory))


if __name__ == '__main__':
    main()