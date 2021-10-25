#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/10 - part 2


from collections import defaultdict
from math import gcd, acos, sqrt

# (11, 11) position yields most asteroids: 221, from part1


def get_input(file_path):
    with open(file_path) as f:
        return [[c for c in line.strip()] for line in f.readlines()]


def circle_and_destroy(board, station_position, destroyed_cnt, vec_map):
    x, y = station_position
    x_range = len(board[0])
    y_range = len(board)
    for quadrant in sorted(vec_map):
        for vec_x, vec_y in vec_map[quadrant]:
            temp_x, temp_y = x, y
            while True:
                temp_x, temp_y = temp_x + vec_x, temp_y + vec_y
                # i'm out
                if temp_x not in range(x_range) or temp_y not in range(y_range):
                    break
                # nothing here
                if board[temp_y][temp_x] == '.':
                    continue
                # an asteroid
                destroyed_cnt += 1
                if destroyed_cnt == 200:
                    print(f"x: {temp_x}; y: {temp_y}")
                    raise StopIteration
                board[temp_y][temp_x] = "."
                break
    return destroyed_cnt


def get_vector_map(board, station_position):
    x, y = station_position
    vec_map = defaultdict(set)
    x_range = len(board[0])
    y_range = len(board)
    # watch out on quadrants!
    for ax_y in range(y_range):
        for ax_x in range(x_range):
            if (ax_x, ax_y) == (x, y):
                continue
            del_x, del_y = ax_x - x, ax_y - y
            xy_gcd = gcd(del_x, del_y)
            _vec = (del_x // xy_gcd, del_y // xy_gcd)
            if ax_y <= y and ax_x >= x:
                vec_map[1].add(_vec)
            elif ax_y > y and ax_x >= x:
                vec_map[2].add(_vec)
            elif ax_y >= y and ax_x < x:
                vec_map[3].add(_vec)
            elif ax_y < y and ax_x < x:
                vec_map[4].add(_vec)
    return vec_map


def by_first_quadrant(vector):
    vec_len = sqrt(sum(i ** 2 for i in vector))
    dot_product = -vector[1]
    return acos( dot_product / vec_len )

def by_second_quadrant(vector):
    vec_len = sqrt(sum(i ** 2 for i in vector))
    dot_product = vector[0]
    return acos( dot_product / vec_len )


def by_third_quadrant(vector):
    vec_len = sqrt(sum(i ** 2 for i in vector))
    dot_product = vector[1]
    return acos( dot_product / vec_len )


def by_fourth_quadrant(vector):
    vec_len = sqrt(sum(i ** 2 for i in vector))
    dot_product = -vector[0]
    return acos( dot_product / vec_len )


def main():
    input_file = 'input.txt'
    board = get_input(input_file)
    station_position = (11, 11)
    vec_map = get_vector_map(board, station_position)
    vec_map[1] = sorted(vec_map[1], key=by_first_quadrant)
    vec_map[2] = sorted(vec_map[2], key=by_second_quadrant)
    vec_map[3] = sorted(vec_map[3], key=by_third_quadrant)
    vec_map[4] = sorted(vec_map[4], key=by_fourth_quadrant)
    destroyed_cnt = 0
    while True:
        try:
            destroyed_cnt = circle_and_destroy(board, station_position, destroyed_cnt, vec_map)
        except StopIteration:
            break


if __name__ == "__main__":
    main()
