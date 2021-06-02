#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/3#part2 - part 2
import re
from collections import defaultdict


def get_input(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip().split(',')


def get_graph(wire, step_counter = 0):
    current_pos = (0, 0)
    wire_graph = set()
    for step in wire:
        dots = operate(step, current_pos, step_counter)
        for dot in dots:
            wire_graph.add(dot)
        current_pos = dots[-1]
    return wire_graph


def operate(step, temp_position, step_counter):
    re_groups = re.search(r'(\w{1})(\d+)', step)
    direction = re_groups.group(1)
    path = int(re_groups.group(2))
    dots = []
    for i in range(path + 1):
        step_counter += 1
        if direction == "R":
            dots.append((i + temp_position[0], temp_position[1], step_counter))
        elif direction == "L":
            dots.append((temp_position[0] - i, temp_position[1], step_counter))
        elif direction == "U":
            dots.append((temp_position[0], temp_position[1] + i, step_counter))
        elif direction == "D":
            dots.append((temp_position[0], temp_position[1] - i, step_counter))
    return dots


def get_stops(wire_input):
    current_position = (0, 0)
    dots = []
    dots.append(current_position)
    for step in wire_input:
        re_groups = re.search(r'(\w{1})(\d+)', step)
        direction = re_groups.group(1)
        path = int(re_groups.group(2))
        if direction == "R":
            current_position = (current_position[0] + path, current_position[1])
            dots.append(current_position)
        elif direction == "L":
            current_position = (current_position[0] - path, current_position[1])
            dots.append(current_position)
        elif direction == "U":
            current_position = (current_position[0], current_position[1] + path)
            dots.append(current_position)
        elif direction == "D":
            current_position = (current_position[0], current_position[1] - path)
            dots.append(current_position)
    return dots


def get_steps_for(intersection, wire_stops):
    if intersection in wire_stops:
        it_index = wire_stops.index(intersection) + 1




def main():
    file_path = "input.txt"
    wireA, wireB = list(get_input(file_path))[0], list(get_input(file_path))[1]
    wireA_graph = get_graph(wireA)
    wireB_graph = get_graph(wireB)
    wireA_inter = set((pos[0], pos[1]) for pos in wireA_graph)
    wireB_inter = set((pos[0], pos[1]) for pos in wireB_graph)
    intersections = wireA_inter.intersection(wireB_inter)
    wireA_stops = get_stops(wireA)
    wireB_stops = get_stops(wireB)
    temp_map = {0: wireA_stops,
                1: wireB_stops
            }
    import pdb
    pdb.set_trace()
    intersections_to_steps_map = defaultdict(dict)
    for i in range(2):
        for it in intersections:
            intersections_to_steps_map[i][it] = get_steps_for(it, temp_map[i])



if __name__ == "__main__":
    print(main())
