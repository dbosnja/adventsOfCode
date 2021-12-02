#!/bin/python3

def get_input(file_path):
    map = []
    with open(file_path) as f:
        for line in f:
            direction, value = line.strip().split()
            map.append((direction, int(value)))
    return map


def main():
    file_path = 'input.txt'
    directions = get_input(file_path)
    forward, depth, aim = 0, 0, 0
    for dir, val in directions:
        if dir == 'up':
            aim -= val
        elif dir == 'down':
            aim += val
        elif dir == 'forward':
            forward += val
            depth += aim * val
    print(forward * depth)


if __name__ == '__main__':
    main()