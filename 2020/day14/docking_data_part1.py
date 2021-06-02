#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/14 - part one

import re


def get_program_instructions(file_path):
    """get list of instructions from input file

    rtype: list
    """
    with open(file_path) as f:
        return f.readlines()


def mask_value(value, mask):
    """mask the value

    :param value: value to be masked and saved -->int
    :param mask: 36 bit mask --> list of chars
    :rtype: int
    """
    value_bin = [int(char) for char in f"{value:036b}"]
    for i, mask_bit in enumerate(mask):
        if mask_bit == "X": continue
        elif mask_bit == "1":
            value_bin[i] = int(mask_bit) or value_bin[i]
        else:
            value_bin[i] = int(mask_bit) and value_bin[i]
    value_bin = list(map(str, value_bin))
    return int(''.join(value_bin), 2)


def main():
    file_path = "input.txt"
    instructions = get_program_instructions(file_path)
    memory = {}
    for instruction in instructions:
        if "mask" in instruction:
            mask = re.search(r"mask\s*=\s*(.+)", instruction).group(1).strip()
        else:
            mem_address, value = re.findall(
                    r"mem\[(\d+)\]\s*=\s*(\d+)", instruction).pop()
            memory[mem_address.strip()] = mask_value(int(value.strip()), mask)
    return sum(memory.values())


if __name__ == "__main__":
    resulting_sum = main()
    print(f"{resulting_sum}")
