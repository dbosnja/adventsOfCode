#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/16 - part one

from collections import defaultdict


def read_input_file(file_path):
    """read the input file

    :param file_path: file path to input file --> str
    :rtype: list
    """
    with open(file_path) as f:
        return f.read()


def get_content(content):
    """return a list of 2 tuples representing the ranges

    :param content: example: 48-425 or 451-952
    :rtype: list
    """
    ranges = []
    for pair in content.split("or"):
        start, end = list(map(str.strip, pair.split("-")))
        ranges += list(range(int(start), int(end) + 1))
    return ranges


def get_invalid_values(ticket, ticket_rules):
    """return a list of all invalid values on one ticket

    :param ticket: a list of ints representing one ticket field values
    :param ticket_rules: dict
    :rtype: list
    """
    invalids = []
    for value in ticket:
        if not is_valid(value, ticket_rules):
            invalids.append(value)
    return invalids


def is_valid(value, ticket_rules):
    """return False if value valid

    :param ticket_rules: dict
    :param value: int
    :rtype: bool
    """
    for range_value in ticket_rules.values():
        if value in range_value:
            return True
    return False


def main():
    file_path = "input.txt"
    input_text = read_input_file(file_path)
    rules, rest = input_text.split("your ticket:")
    my_ticket, nearby_tickets = rest.split("nearby tickets:")
    rules = rules.strip()
    ticket_rules = {}
    for line in rules.split("\n"):
        key, content = line.split(":")
        ticket_rules[key] = get_content(content)
    my_ticket = list(map(int, my_ticket.strip().split(",")))
    nearby_tickets = nearby_tickets.strip().split("\n")
    other_tickets = [tuple(map(int, ticket.strip().split(",")))
                    for ticket in nearby_tickets]
    # the data is loaded
    invalid_values = []
    for ticket in other_tickets:
        invalid_values.extend(get_invalid_values(ticket, ticket_rules))
    return sum(invalid_values)


if __name__ == "__main__":
    print(main())
