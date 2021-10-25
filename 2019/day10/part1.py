#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/10 - part 1


from math import gcd


def get_input(file_path):
    with open(file_path) as f:
        return [i.strip() for i in f.readlines()]


def count_asteroids(board, x, y):
    x_range = len(board[0])
    y_range = len(board)
    unique_vector_set = get_vector_set(board, x, y)
    asteroid_cnt = 0
    for vec_x, vec_y in unique_vector_set:
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
            asteroid_cnt += 1
            break
    return asteroid_cnt


def get_vector_set(board, x, y):
    vec_set = set()
    x_range = len(board[0])
    y_range = len(board)
    for ax_y in range(y_range):
        for ax_x in range(x_range):
            if (ax_x, ax_y) == (x, y):
                continue
            del_x, del_y = ax_x - x, ax_y - y
            xy_gcd = gcd(del_x, del_y)
            vec_set.add((del_x // xy_gcd, del_y // xy_gcd))
    return vec_set


def main():
    input_file = 'input.txt'
    board = get_input(input_file)
    position_count = {}
    x_range = len(board[0])
    y_range = len(board)
    for y in range(y_range):
        for x in range(x_range):
            if board[y][x] == '.':
                continue
            position_count[(x, y)] = count_asteroids(board, x, y)
    return max(position_count.values())


if __name__ == "__main__":
    print(f"{main()}")
