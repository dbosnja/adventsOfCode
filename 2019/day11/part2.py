#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/11 - part 2

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
    pos_to_color[position] = 1
    while True:
        in_value = pos_to_color[position]
        try:
            color, instr_set, ptr_instr, rel_base = complete_intcode.main(instr_set, ptr_instr, rel_base, in_value)
            direction, instr_set, ptr_instr, rel_base = complete_intcode.main(instr_set, ptr_instr, rel_base, in_value)
        except StopIteration:
            break
        else:
            pos_to_color[position] = color
            head_ptr = rotate(head_ptr, direction)
            position = position[0] + head_ptr[0], position[1] + head_ptr[1]
    psk = sorted(pos_to_color.keys())
    min_x, max_x = min(x for x, _ in psk), max(x for x, _ in psk)
    min_y = min(y for x, y in psk if x == min_x)
    max_y = max(y for x, y in psk if x == min_x)
    for y in range(max_y + 1 , min_y - 3, -1):
        for x in range(min_x, max_x):
            if pos_to_color[(x, y)] == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()


if __name__ == "__main__":
    main()
