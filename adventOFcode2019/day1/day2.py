#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/1 - part 1
from math import floor

def get_input(file_path):
    fuel_sum = 0
    with open(file_path) as f:
        for line in f:
            fuel_sum += compute(int(line.strip()))
    return fuel_sum


def compute(line):
    fuels = []
    while floor(line / 3) - 2 > 0:
        line = floor(line / 3) - 2
        fuels.append(line)
    return sum(fuels)


def main():
    file_path = "input.txt"
    return get_input(file_path)


if __name__ == "__main__":
    print(f"{main()}")
