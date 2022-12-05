def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            first, second = line.strip().split(',')
            first_l, first_r = [int(i) for i in first.split('-')]
            second_l, second_r = [int(i) for i in second.split('-')]
            yield first_l, first_r, second_l, second_r


def main():
    in_file = 'input.txt'
    total_sum = 0
    for first_l, first_r, second_l, second_r in get_input(in_file):
        if second_l <= first_l and second_r >= first_r or first_l <= second_l and first_r >= second_r:
            total_sum += 1
    print(total_sum)

main()