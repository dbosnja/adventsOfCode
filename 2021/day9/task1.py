#!/bin/python3

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


def main():
    file_path = 'input.txt'
    heights = get_input(file_path)
    row_cnt, col_cnt = len(heights), len(heights[0])
    low_points = []
    low_pts_cnt = 0
    for i, j in product(range(row_cnt), range(col_cnt)):
        if is_low_point(i, j, heights, row_cnt, col_cnt):
            low_points.append(int(heights[i][j]))
            low_pts_cnt += 1
    print(low_pts_cnt + sum(low_points))


if __name__ == '__main__':
    main()