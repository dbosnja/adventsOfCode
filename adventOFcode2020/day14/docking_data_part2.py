#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/14 - part one

import re
from itertools import product


def get_program_instructions(file_path):
    """get list of instructions from input file

    rtype: list
    """
    with open(file_path) as f:
        return f.readlines()


def get_mem_adresses(address, mask):
    """mask the value

    :param address: address to be masked and returned --> int
    :param mask: 36 bit mask --> list of chars
    :rtype: list
    """
    address_bin = [int(char) for char in f"{address:036b}"]
    for i, mask_bit in enumerate(mask):
        if mask_bit == "0": continue
        elif mask_bit == "1":
            address_bin[i] = address_bin[i] or int(mask_bit)
        else:
            address_bin[i] = "X"
    address_bin = ''.join(list(map(str, address_bin)))
    tmp_address_bin = address_bin
    space_of_combos = product((0, 1), repeat=address_bin.count("X"))
    resulting_addresses = []
    for element in space_of_combos:
        for coordinate in element:
            tmp_address_bin = tmp_address_bin.replace("X", str(coordinate), 1)
        resulting_addresses.append(tmp_address_bin)
        tmp_address_bin = address_bin
    return resulting_addresses


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
            for mem_adrs in get_mem_adresses(int(mem_address), mask):
                memory[mem_adrs] = int(value)
    return sum(memory.values())


if __name__ == "__main__":
    resulting_sum = main()
    print(f"{resulting_sum}")
