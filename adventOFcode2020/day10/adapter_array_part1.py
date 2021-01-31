#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/10 - part 1

from functools import reduce
from collections import defaultdict


def get_input_file(file_path):
    """read input file and return a list of port output jolts

    :param file_path: file path to input file --> str
    :rtype: list
    """
    with open(file_path) as f:
        port_output = [int(line.strip()) for line in f]
    return port_output


def main():
    file_path = "input.txt"
    port_outputs = get_input_file(file_path)
    # my device's built-in adapter is always 
    # 3 higher than the highest adapter
    my_extra_jolts = 3 + max(port_outputs)
    starting_jolt = 0
    extended_port_outputs = port_outputs + [starting_jolt, my_extra_jolts]
    extended_port_outputs = sorted(extended_port_outputs)
    req_diff1, req_diff2 = 1, 3
    count_diffs = defaultdict(int)
    joltage_diffs = [right_joltage - left_joltage
                    for left_joltage, right_joltage in 
                    zip(extended_port_outputs[:-1], extended_port_outputs[1:])]
    for it in joltage_diffs: count_diffs[it] += 1
    return count_diffs[req_diff1] * count_diffs[req_diff2]


if __name__ == "__main__":
    resulting_product = main()
    print(f"{resulting_product}")
