#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/6 - part two
from collections import defaultdict
from functools import reduce


def get_all_group_answers(file_path):
    """read the input file and return the sum of answers by each group
    
    :param file_path: str
    :rtype: int
    """
    with open(file_path) as f:
        return get_number_of_answers(f.readlines())


def get_number_of_answers(list_of_input_lines):
    """get number of answers answered by all peeps in the plane

    :param list_of_input_lines: list of input lines
    :rtype: int
    """
    a_group = []
    total_sum = 0
    for line in list_of_input_lines:
        if not line.strip():
           total_sum += get_for_one_group(a_group)
           a_group = []
        else:
            a_group.append(line.strip())
    total_sum += get_for_one_group(a_group)
    return total_sum
    

def get_for_one_group(group_answers):
    """get number of answers answered by all peeps in the group

    :param group_answers: list of answers by one group
    :rtype: int
    """
    all_group_answers = defaultdict(set)
    for i, line in enumerate(group_answers):
        for char in line:
            all_group_answers[i].add(char)
    return len(reduce(set.intersection, all_group_answers.values()))



def main():
    file_path = "input.txt"
    print(f"{get_all_group_answers(file_path)}")


if __name__ == "__main__":
    main()
    