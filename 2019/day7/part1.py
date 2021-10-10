#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/7 - part 1

from itertools import permutations

import op_code_part1


def get_input(file_path):
    with open(file_path) as f:
        return [int(i) for i in f.read().strip().split(",")]


def main():
    file_path = "input.txt"
    instruction_set = get_input(file_path)
    thruster_values = []
    for p in permutations(range(5)):
        a_input = 0
        for phase in p:
            a_output = op_code_part1.main(phase, a_input, list(instruction_set))
            a_input = a_output
        thruster_values.append(a_output)
    return max(thruster_values)


if __name__ == "__main__":
    print(f"{main()}")
