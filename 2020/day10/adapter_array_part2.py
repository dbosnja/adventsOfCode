#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/10#part2

from time import time
from collections import defaultdict


def get_input_file(file_path):
    """read input file and return a list of port output jolts

    :param file_path: file path to input file --> str
    :rtype: list
    """
    with open(file_path) as f:
        port_output = [int(line.strip()) for line in f]
    return port_output


def get_children(node, main_list):
    """set node's children to an empty list or
       to a list of Nodes according to rules

    :param node: current node being added children --> int
    :param main_list: list of all port outputs
    :rtype: list
    """
    allowed_diff = 3
    # main_list is sorted --> better use binary_chop if you like your computer.
    # with help of binary_chop we find the index of the element with the same
    # value as node.name, and augment it
    first_index = binary_chop(node, main_list) + 1
    children = []
    while True:
        children.append(main_list[first_index])
        first_index += 1
        # we're out of the list range
        if first_index >= len(main_list) - 1: break
        # we're out of candidates for this node's children
        if main_list[first_index] - node > allowed_diff: break
    # due to the modelling rules, this list is small; 3 elements at most
    return children


def binary_chop(joltage, main_list):
    """return the index of the joltage element in the given list.
       uses binary search --> O(n)=log(n) --> extremely fast

    :param joltage: int
    :param main_list: list of int
    :rtype: int
    """
    start_index = 0
    end_index = len(main_list) - 1
    while start_index != end_index:
        half_the_list = (start_index + end_index) // 2  # O(1)
        list_middle_value = main_list[half_the_list]  # O(1)
        if joltage == list_middle_value:  # O(1)
            return half_the_list
        elif joltage > main_list[half_the_list]:  # O(1)
            start_index = half_the_list + 1
        else:
            end_index = half_the_list - 1  # O(1)
    # at this moment start_index equals to end_index
    return start_index


def main():
    file_path = "input.txt"
    port_outputs = get_input_file(file_path)
    # my device's built-in adapter is always
    # 3 higher than the highest adapter
    my_extra_jolts = 3
    starting_jolt = 0
    edge_outputs = [starting_jolt, my_extra_jolts + max(port_outputs)]
    # all port outputs together with my device's and default wall output
    # sorted ascendingly
    extended_port_outputs = sorted(port_outputs + edge_outputs)
    pre_joltage_occurrences = defaultdict(int)
    # this is always the beginning of an adapters sequence
    pre_joltage_occurrences[0] = 1
    # whenever we hit this milestone, we have one arrangement combination more
    size_to_reach = extended_port_outputs[-1]
    # represents the main sought value -> the number of arrangement combinations
    number_of_arrangements = 0
    # represents "tree level" on which the program is actually based on
    # defining pre_joltage_occurrences was level 0
    tree_level = 1
    while True:
        start_time = time()
        # this containter simulates workflow of .zip algorithms
        # it's created from the pre_joltage_occurrences
        post_joltage_occurrences = defaultdict(int)
        for joltage, occurences in pre_joltage_occurrences.items():
            for child in get_children(joltage, extended_port_outputs):
                if child == size_to_reach:
                    number_of_arrangements += occurences
                    continue
                # else we have to count occurences
                # counting the joltage which produced them
                post_joltage_occurrences[child] += occurences
        if not post_joltage_occurrences: break
        pre_joltage_occurrences = post_joltage_occurrences
        level_time = time() - start_time
        tree_level += 1
        print(f"current tree level setup running time: {level_time:0.3e}s")
        print(f'last "tree level" size: {len(post_joltage_occurrences)}')
        print(f'current "tree depth": {tree_level}\n')
    return number_of_arrangements


if __name__ == "__main__":
    number_of_arrangements = main()
    print(f"{number_of_arrangements}")
