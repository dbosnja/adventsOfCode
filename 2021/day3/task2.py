#!/bin/python3

from collections import defaultdict

def get_input(file_path):
    with open(file_path) as f:
       binaries = [line.strip() for line in f]
    return binaries


def main():
    file_path = 'input.txt'
    binaries = get_input(file_path)
    binaries_cpy = binaries[:]
    col_cnt = len(binaries[0])
    done = False
    for i in range(col_cnt):
        if done:
            break
        ith_rate = defaultdict(int)
        for row in binaries_cpy:
            if row[i] == '1':
                ith_rate['1'] += 1
            else:
                ith_rate['0'] += 1
        look_for = '1' if ith_rate['1'] >= ith_rate['0'] else '0'
        for row in binaries_cpy[:]:
            if row[i] != look_for:
                binaries_cpy.remove(row)
                if len(binaries_cpy) == 1:
                    done = True
                    oxygen_rate = binaries_cpy.pop()
                    break
    done = False
    binaries_cpy = binaries[:]
    for i in range(col_cnt):
        if done:
            break
        ith_rate = defaultdict(int)
        for row in binaries_cpy:
            if row[i] == '1':
                ith_rate['1'] += 1
            else:
                ith_rate['0'] += 1
        look_for = '0' if ith_rate['0'] <= ith_rate['1'] else '1'
        for row in binaries_cpy[:]:
            if row[i] != look_for:
                binaries_cpy.remove(row)
                if len(binaries_cpy) == 1:
                    done = True
                    co2_rate = binaries_cpy.pop()
                    break

    oxygen_rate = f'0b{oxygen_rate}'
    co2_rate = f'0b{co2_rate}'
    print(int(oxygen_rate, 2) * int(co2_rate, 2))


if __name__ == '__main__':
    main()