#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/2#part2 - part 2

from itertools import product


def get_input(file_path):
    with open(file_path) as f:
        return list(map(int, f.read().split(",")))


def main():
    file_path = "input.txt"
    for p, r in product(range(100), range(100)):
        codes = get_input(file_path)
        codes[1], codes[2] = p, r
        for i in range(0, len(codes), 4):
            if codes[i] == 99:
                break
            elif codes[i] == 1:
                codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
            elif codes[i] == 2:
                codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
        if codes[0] == 19690720: return p, r


if __name__ == "__main__":
    prod = main()
    print(f"{100 * prod[0] + prod[1]}")
