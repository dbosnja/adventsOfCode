#! /usr/bin/python3.9
#https://adventofcode.com/2020/day/7
import re
from collections import defaultdict


def get_input_file(file_path):
    """read input file and return mapping rules for each
       type of a bag

    :param file_path: file path to input file --> str
    :return: defaultdict(list)
    """
    bags_container = defaultdict(list)
    with open(file_path) as f:
        for line in f:
            bag, bag_content = line.strip().split("bags", 1)
            bags_container[bag.strip()].extend(get_bag_content(bag_content))
    return bags_container


def get_bag_content(bag_content):
    """get all bag types which are held by some bag

    :param bag_content: string containing content of the outermost bag
    :return: [(),(),..,()]
    :rtype: list
    """
    bag_content = bag_content.split("contain")[-1].strip(" .")
    number_and_bag_type = []
    for item in bag_content.split(","):
        try:
            bag_number = re.search(r"\d{1}", item.strip()).group()
        except AttributeError:
            # outermost bag contains nothing
            return [()]
        type_of_bag = item.replace(bag_number, "").split('bag')[0].strip()
        number_and_bag_type.append((bag_number, type_of_bag))
    return number_and_bag_type


def it_holds_directly(bag_content, bag_to_look_for):
    """return True if shiny gold bag is held in this bag_content

    :param bag_content: list of bags outer bag contains
    :param bag_to_look_for: str
    :rtype: bool
    """
    # this bag contains no other bag
    if not bag_content[0]: return False
    # otherwise check if there's shiny gold bag
    for _, bag in bag_content:
        if bag_to_look_for == bag: return True
    return False

def main():
    file_path = "input.txt"
    bag_to_look_for = "shiny gold"
    bags_mapping = get_input_file(file_path)
    print(bags_mapping)
    number_of_shiny_bag_containters = 0
    for key_bag in bags_mapping:
        if it_holds_directly(bags_mapping[key_bag], bag_to_look_for):
            number_of_shiny_bag_containters += 1
            continue
        # bag_key does not hold shiny gold bag directly
        # we need to check if some of the bag_key's innermost bag does



    print("number of shiny gold bag containers: {}".format(number_of_shiny_bag_containters))


if __name__ == "__main__":
    main()