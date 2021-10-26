#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/11 - part 1

from typing import DefaultDict
import complete_intcode


def get_input(file_path):
    with open(file_path) as f:
        return [int(i) for i in f.read().strip().split(",")]


def rotate(head_ptr, direction):
    head_x, head_y = head_ptr
    return (-head_y, head_x) if not direction else (head_y, -head_x)



def main():
    input_file = 'input.txt'
    instr_set = get_input(input_file)
    instr_set += [0 for i in range(1000)]
    ptr_instr = rel_base = 0
    position = (0, 0)
    head_ptr = (0, 1)
    pos_to_color = DefaultDict(int)
    pos_visit_set = set()
    while True:
        in_value = pos_to_color[position]
        try:
            color, instr_set, ptr_instr, rel_base = complete_intcode.main(instr_set, ptr_instr, rel_base, in_value)
            direction, instr_set, ptr_instr, rel_base = complete_intcode.main(instr_set, ptr_instr, rel_base, in_value)
        except StopIteration:
            break
        else:
            pos_to_color[position] = color
            pos_visit_set.add(position)
            head_ptr = rotate(head_ptr, direction)
            position = position[0] + head_ptr[0], position[1] + head_ptr[1]
    return len(pos_visit_set)


if __name__ == "__main__":
    print(f"{main()}")
