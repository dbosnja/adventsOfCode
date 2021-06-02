#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/16#part2

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


def is_ticket_valid(ticket, ticket_rules):
    """return True if ticket is valid

    :param ticket: a list of ints representing one ticket field values
    :param ticket_rules: dict
    :rtype: bool
    """
    for value in ticket:
        if not is_valid(value, ticket_rules):
            return False
    return True


def is_valid(value, ticket_rules):
    """return True if value valid

    :param ticket_rules: dict
    :param value: int
    :rtype: bool
    """
    for range_value in ticket_rules.values():
        if value in range_value:
            return True
    return False


def get_field_definitions(all_columns, ticket_rules):
    """calculcate how many columns satisify the rules

    :param all_columns: all columns in all ticket field values
    :param ticket_rules: dict
    :rtype: defauldict(list)
    """
    definitions = defaultdict(list)
    for i, col in enumerate(all_columns):
        for key, ranges in ticket_rules.items():
            if all(c in ranges for c in col):
                definitions[i].append(key)
    return definitions


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
    my_ticket = tuple(map(int, my_ticket.strip().split(",")))
    nearby_tickets = nearby_tickets.strip().split("\n")
    other_tickets = [tuple(map(int, ticket.strip().split(",")))
                    for ticket in nearby_tickets]
    # the data is loaded
    for ticket in other_tickets[:]:
        if not is_ticket_valid(ticket, ticket_rules):
            # discard the invalid tickets
            other_tickets.remove(ticket)
    # let's collect all columns from all ticket fields
    other_tickets.append(my_ticket)
    all_columns = []
    for i in range(len(my_ticket)):
        temp_column = [ticket[i] for ticket in other_tickets]
        all_columns.append(tuple(temp_column))
    definitions = get_field_definitions(all_columns, ticket_rules)
    unique_definitions = {}
    while True:
        if not any(bool(value) for value in definitions.values()):
            # we emptied the definitions
            break
        for position, fields in definitions.items():
            if len(fields) == 1:
                # better save it
                unique_field = fields.pop()
                unique_definitions[unique_field] = position
                break
        for _, fields in definitions.items():
            if unique_field in fields:
                fields.remove(unique_field)
    prod = 1
    for field, position in unique_definitions.items():
        if field.startswith('departure'):
            prod *= my_ticket[position]
    return prod

if __name__ == "__main__":
    print(main())
