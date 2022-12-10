def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            if 'noop' in line:
                yield line.strip(), 0
            else:
                opcode, scalar = line.strip().split()
                yield opcode, int(scalar)


def main():
    in_file = 'input.txt'
    x = 1
    cycle_cnt = 1
    total_sum = 0
    for opcode, scalar in get_input(in_file):
        if opcode == 'noop':
            if cycle_cnt in [20, 60, 100, 140, 180, 220]:
                total_sum += x * cycle_cnt
            cycle_cnt += 1
        else:
            if cycle_cnt in [20, 60, 100, 140, 180, 220]:
                total_sum += x * cycle_cnt
            cycle_cnt += 1
            if cycle_cnt in [20, 60, 100, 140, 180, 220]:
                    total_sum += x * cycle_cnt
            x += scalar
            cycle_cnt += 1            
    print(total_sum)


main()