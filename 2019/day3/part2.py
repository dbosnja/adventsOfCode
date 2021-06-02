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
    total_steps = 0
    if intersection in wire_stops:
        it_index = wire_stops.index(intersection) + 1
        passed_steps = wire_stops[:it_index]
        for step in slices(passed_steps):
            total_steps += abs(step[0][0] - step[1][0])
            total_steps += abs(step[0][1] - step[1][1])
        return total_steps
    for step in slices(wire_stops):
        if intersection[0] in range(min(step[0][0], step[1][0]), max(step[0][0], step[1][0]) + 1)\
            and intersection[1] in range(min(step[0][1], step[1][1]), max(step[0][1], step[1][1]) + 1):
            last_step = wire_stops.index(step[0])
            break
    passed_steps = wire_stops[:last_step + 1]
    for step in slices(passed_steps):
        total_steps += abs(step[0][0] - step[1][0])
        total_steps += abs(step[0][1] - step[1][1])
    total_steps += abs(wire_stops[last_step][0] - intersection[0])
    total_steps += abs(wire_stops[last_step][1] - intersection[1])
    return total_steps


def slices(a_list):
    temp_list = []
    for i, _ in enumerate(a_list):
        if i == len(a_list) - 1:
            break
        temp_list.append(a_list[i:i + 2])
    return temp_list


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
    intersections_to_steps_map = defaultdict(dict)
    for i in range(2):
        for it in intersections:
            if it == (0, 0):
                continue
            intersections_to_steps_map[i][it] = get_steps_for(it, temp_map[i])
    steps = []
    intersections.remove((0, 0))
    for it in intersections:
        intersection_length = intersections_to_steps_map[0][it]\
                              + intersections_to_steps_map[1][it]
        steps.append(intersection_length)
    return min(steps)


if __name__ == "__main__":
    print(main())