from string import ascii_lowercase, ascii_uppercase

lowercase_prio = {item: i + 1 for i, item in enumerate(ascii_lowercase)}
uppercase_prio = {item: i + 27 for i, item in enumerate(ascii_uppercase)}


def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            yield line.strip()


def main():
    in_file = 'input.txt'
    total_sum = 0
    for rucksak in get_input(in_file):
        ruck_ln = len(rucksak)
        common_types = set(rucksak[:ruck_ln // 2]).intersection(set(rucksak[ruck_ln // 2:]))
        for item in common_types:
            if item in lowercase_prio:
                total_sum += lowercase_prio[item]
            elif item in uppercase_prio:
                total_sum += uppercase_prio[item]
    print(total_sum)


main()