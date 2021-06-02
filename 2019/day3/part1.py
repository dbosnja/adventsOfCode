#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/3 - part 1
import re


def get_input(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip().split(',')


def get_graph(wire):
    current_pos = (0, 0)
    wire_graph = set()
    for step in wire:
        dots = operate(step, current_pos)
        for dot in dots:
            wire_graph.add(dot)
        current_pos = dots[-1]
    return wire_graph


def operate(step, temp_position):
    re_groups = re.search(r'(\w{1})(\d+)', step)
    direction = re_groups.group(1)
    path = int(re_groups.group(2))
    dots = []
    for i in range(path + 1):
        if direction == "R":
            dots.append((i + temp_position[0], temp_position[1]))
        elif direction == "L":
            dots.append((temp_position[0] - i, temp_position[1]))
        elif direction == "U":
            dots.append((temp_position[0], temp_position[1] + i))
        elif direction == "D":
            dots.append((temp_position[0], temp_position[1] - i))
    return dots


def main():
    file_path = "input.txt"
    wireA, wireB = list(get_input(file_path))[0], list(get_input(file_path))[1]
    wireA_graph = get_graph(wireA)
    wireB_graph = get_graph(wireB)
    intersections = wireA_graph.intersection(wireB_graph)
    intersections.remove((0, 0))
    return min(map(lambda x: abs(x[0]) + abs(x[1]), intersections))


if __name__ == "__main__":
    print(main())
