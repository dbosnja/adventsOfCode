#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/8
import re
from collections import defaultdict

accumulator = 0


def get_input_file(file_path):
    """read input file and return a list of boot codes

    :param file_path: file path to input file --> str
    :return: [(),...,()]
    :rtype: list
    """
    boot_code_list = []
    with open(file_path) as f:
        for line in f:
            cmd, arg = map(str.strip, line.strip().split(" "))
            boot_code_list.append((cmd, int(arg)))
    return boot_code_list


def update_accumulator(offset, instruction_index):
    """add offset to the current state of accumulator
    
    :param offset: signed int
    :param instruction_index: current index of the instruction
    :rtype: int
    """
    global accumulator
    accumulator += offset
    return instruction_index


def no_operation(offset, instruction_index):
    """takes an offset and does nothing, 
       ie just return the current instruction_index
    
    :param offset: signed int
    :param instruction_index: current index of the instruction
    :rtype: int
    """
    return instruction_index


def jump(offset, instruction_index):
    """jump from current instruction to one relative to it
       ie. execute instruction on instruction_index + offset line 
    
    :param offset: signed int
    :param instruction_index: current index of the instruction
    :rtype: NoneType
    """
    return instruction_index + offset


def main():
    file_path = "input.txt"
    boot_code_list = get_input_file(file_path)
    instruction_switch = {
        "acc": update_accumulator,
        "nop": no_operation,
        "jmp": jump
    }
    instruction_record = set()
    i = 0
    while True:
        cmd, offset = boot_code_list[i]
        if (i, cmd, offset) in instruction_record: return accumulator
        instruction_record.add((i, cmd, offset))
        instruction_outcome = instruction_switch[cmd](offset, i)
        i = i + 1 if i == instruction_outcome else instruction_outcome


if __name__ == "__main__":
    accumulator = main()
    print(f"{accumulator}")
