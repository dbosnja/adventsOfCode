#!/bin/python3

from itertools import product

vectors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def get_input(file_path):
    grid = []
    with open(file_path) as f:
        for line in f:
            grid.append([int(c) for c in line.strip()])
        return grid


def increase_by_one(octopus_grid):
    for i, j in product(range(len(octopus_grid)), repeat=2):
        octopus_grid[i][j] += 1


def do_the_flashing(octopus_grid, flashed):
    for i, j in product(range(len(octopus_grid)), repeat=2):
        if octopus_grid[i][j] <= 9 or (i, j) in flashed:
            continue
        flash_it(i, j, octopus_grid, flashed)


def flash_it(i, j, octopus_grid, flashed):
    flashed.add((i, j))
    for vec_x, vec_y in vectors:
        tmp_i, tmp_j = i + vec_x, j + vec_y
        if is_out_of_grid(tmp_i, tmp_j, octopus_grid):
            continue
        neighbour_energy = octopus_grid[tmp_i][tmp_j]
        if neighbour_energy < 9:
            octopus_grid[tmp_i][tmp_j] += 1
            continue
        # did it flash already?
        if (tmp_i, tmp_j) in flashed:
            continue
        flash_it(tmp_i, tmp_j, octopus_grid, flashed)


def is_out_of_grid(tmp_i, tmp_j, octopus_grid):
    grid_len = len(octopus_grid)
    return tmp_i < 0 or tmp_i >= grid_len or tmp_j < 0 or tmp_j >= grid_len


def reset_flashed_ones(octopus_grid, flashed):
    for i, j in flashed:
        octopus_grid[i][j] = 0


def main():
    file_path = 'input.txt'
    octopus_grid = get_input(file_path)
    grid_len = len(octopus_grid) ** 2
    step = 0
    while True:
        step += 1
        increase_by_one(octopus_grid)
        flashed = set()
        do_the_flashing(octopus_grid, flashed)
        reset_flashed_ones(octopus_grid, flashed)
        if grid_len == len(flashed):
            print(step)
            break


if __name__ == '__main__':
    main()