from string import ascii_lowercase, ascii_uppercase

lowercase_prio = {item: i + 1 for i, item in enumerate(ascii_lowercase)}
uppercase_prio = {item: i + 27 for i, item in enumerate(ascii_uppercase)}


def get_input(in_file):
    group_items = []
    with open(in_file) as f:
        for line in f:
            group_items.append(line.strip())
            if len(group_items) == 3:
                yield group_items
                group_items = []


def main():
    in_file = 'input.txt'
    total_sum = 0
    for rucksak1, rucksak2, rucksak3 in get_input(in_file):
        common_types = set(rucksak1).intersection(set(rucksak2)).intersection(set(rucksak3))
        for item in common_types:
            if item in lowercase_prio:
                total_sum += lowercase_prio[item]
            elif item in uppercase_prio:
                total_sum += uppercase_prio[item]
    print(total_sum)


main()