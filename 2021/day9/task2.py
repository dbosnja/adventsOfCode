#!/bin/python3

from math import prod
from itertools import product

vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]


def is_low_point(i, j, heights, row_cnt, col_cnt):
    neighbours = []
    point = heights[i][j]
    for vec_x, vec_y in vectors:
        new_i, new_j = i + vec_x, j + vec_y
        if new_i < 0 or new_i >= row_cnt or new_j < 0 or new_j >= col_cnt:
            continue
        neighbours.append(heights[new_i][new_j])
    return all(point < n for n in neighbours)


def get_basin_members(i, j, basin_members, row_cnt, col_cnt, heights):
    basin_members.add((i, j))
    for vec_x, vec_y in vectors:
        new_i, new_j = i + vec_x, j + vec_y
        if new_i < 0 or new_i >= row_cnt or new_j < 0 or new_j >= col_cnt:
            continue
        neighbour = heights[new_i][new_j]
        if (new_i, new_j) in basin_members or neighbour == '9' or neighbour < heights[i][j]:
            continue
        get_basin_members(new_i, new_j, basin_members, row_cnt, col_cnt, heights)


def main():
    file_path = 'input.txt'
    heights = get_input(file_path)
    row_cnt, col_cnt = len(heights), len(heights[0])
    low_points = []
    for i, j in product(range(row_cnt), range(col_cnt)):
        if is_low_point(i, j, heights, row_cnt, col_cnt):
            low_points.append((i, j))
    basins = []
    for low_i, low_j in low_points:
        basin_members = set()
        get_basin_members(low_i, low_j, basin_members, row_cnt, col_cnt, heights)
        basins.append(len(basin_members))
    basins.sort(reverse=True)
    print(prod(basins[:3]))


if __name__ == '__main__':
    main()