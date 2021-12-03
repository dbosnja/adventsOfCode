#!/bin/python3

from collections import defaultdict

def get_input(file_path):
    with open(file_path) as f:
       binaries = [line.strip() for line in f]
    return binaries


def main():
    file_path = 'input.txt'
    binaries = get_input(file_path)
    col_cnt = len(binaries[0])
    rates = []
    for i in range(col_cnt):
        ith_rate = defaultdict(int)
        for row in binaries:
            if row[i] == '1':
                ith_rate['1'] += 1
            else:
                ith_rate['0'] += 1
        rates.append(ith_rate)
    gamma_rate, epsilon_rate = [], []
    for rate in rates:
        if rate['1'] > rate['0']:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')
    gamma = f'0b{"".join(gamma_rate)}'
    epsilon = f'0b{"".join(epsilon_rate)}'
    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()