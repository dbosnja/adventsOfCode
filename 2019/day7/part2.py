#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/7 - part 2

from itertools import permutations
from time import sleep

import op_code_part2


def get_input(file_path):
    with open(file_path) as f:
        return [int(i) for i in f.read().strip().split(",")]


def main():
    file_path = "input.txt"
    instruction_set = get_input(file_path)
    thruster_values = []
    for perm in permutations(range(5, 10)):
        a_input = 0
        ptr = 0
        halt = False
        first_time = True
        instr_maps = {i: list(instruction_set) for i in range(5, 10)}
        ptr_maps = {i: 0 for i in range(5, 10)}
        # start a process
        while True:
            for phase in perm:
                try:
                    if first_time:
                        a_output, ptr, instr_set = op_code_part2.main(a_input, instr_maps[phase], ptr_maps[phase], phase)
                        instr_maps[phase] = instr_set
                        ptr_maps[phase] = ptr
                    else:
                        a_output, ptr, instr_set = op_code_part2.main(a_input, instr_maps[phase], ptr_maps[phase])
                        instr_maps[phase] = instr_set
                        ptr_maps[phase] = ptr
                except StopIteration:
                    halt = True
                    break
                else:
                    # print(f"input:{a_input}, output: {a_output}")
                    a_input = a_output
            first_time = False
            if halt:
                break
        thruster_values.append(a_output)
    return max(thruster_values)


if __name__ == "__main__":
    print(f"{main()}")
