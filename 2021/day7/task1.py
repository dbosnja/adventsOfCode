#!/bin/python3


def get_input(file_path):
    with open(file_path) as f:
        return [int(c) for c in f.readline().strip().split(',')]


def get_distance(num, crab_positions):
    dist_sum = 0
    for i in crab_positions:
        dist_sum += abs(num - i)
    return dist_sum


def main():
    file_path = 'input.txt'
    crab_positions = get_input(file_path)
    min_pos, max_pos = min(crab_positions), max(crab_positions)
    distances = []
    for i in range(min_pos, max_pos + 1):
        distances.append(get_distance(i, crab_positions))
    print(min(distances))



if __name__ == '__main__':
    main()