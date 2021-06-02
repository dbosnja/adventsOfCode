#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/19#part2

from itertools import product
from functools import reduce


def get_tasks(file_path):
    """read the input file

    :param file_path: file path to input file --> str
    :rtype: tuple
    """
    rules = {}
    msgs = []
    with open(file_path) as f:
        input_lines = f.readlines()
    for line in input_lines:
        if ":" in line:
            key, value = tuple(map(str.strip, line.split(":")))
            rules[key] = value
        else:
            if not line.strip(): continue
            msgs.append(line.strip())
    rules = {int(k): get_rule(k, rules) for k in sorted(rules.keys(), key=int)}
    print(len(msgs))
    return rules, msgs


def get_rule(key, rules):
    """
    :param key: int
    :param rules: dict holding all the rules
    :rtype: list
    """
    rule = rules[key].strip()
    rule_list = []
    if "|" not in rule:
        sort_of_rule = rule.split(" ")
        if len(sort_of_rule) > 1:
            rule_list.append(tuple(map(int, sort_of_rule)))
        else:
            try:
                rule_list.append(tuple(map(int, sort_of_rule)))
            except ValueError:
                rule_list.append((rule.strip('" '),))
    else:
        for item in rule.strip().split("|"):
            if not item.strip(): continue
            rule_list.append(tuple(map(int, item.strip().split(" "))))
    return rule_list


def get_rules(rules, rule_id):
    """recursion for gathering 'all' combinations of rules

    :param: rule id --> int
    :param rules: dict holding all rules
    :rtype: list
    """
    combinations_list = []
    for combo_tuple in rules[rule_id]:
        if type(combo_tuple[0]) != int:
            # recursion ends
            combinations_list.append(combo_tuple[0])
            return combinations_list
        # recursion(s) begin(s)
        rules_applied = [get_rules(rules, position) for position in combo_tuple]
        combinations_list.extend(reduce(product_and_connect, rules_applied))
    return combinations_list


def product_and_connect(combo1, combo2):
    """create a Kartesiev product of combo1, and combo2 join it and
       return as one container of all possible combinations

    :param combo1: all possible combinations returned by get_rules for some rule_id --> list
    :param combo2: all possible combinations returned by get_rules for some rule_id --> list
    rtype: list
    """
    return list(map(''.join, list(product(combo1, combo2))))


def main():
    file_path = "input.txt"
    rules, messages = get_tasks(file_path)
    # data loaded
    all_rules = get_rules(rules, 0)
    import pdb; pdb.set_trace()
    valid_msgs = [int(message in all_rules) for message in messages]
    return sum(valid_msgs)


if __name__ == "__main__":
    print(main())
