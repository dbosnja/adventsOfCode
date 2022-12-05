def get_input(in_file):
    i = 1
    cal_map = {}
    cal_sum = 0
    with open(in_file) as f:
        for line in f:
            if not line.strip():
                cal_map[i] = cal_sum
                i += 1
                cal_sum = 0
            else:
                cal_sum += int(line)
    return cal_map


def main():
    in_file = 'input.txt'
    cal_map = get_input(in_file)
    max_cal = sum(sorted(cal_map.values(), reverse=True)[:3])
    print(max_cal)


main()