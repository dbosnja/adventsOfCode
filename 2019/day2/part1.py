#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/2 - part 1

def get_input(file_path):
    with open(file_path) as f:
        return list(map(int, f.read().split(",")))


def main():
    file_path = "input.txt"
    codes = get_input(file_path)
    for i in range(0, len(codes), 4):
        if codes[i] == 99:
            break
        elif codes[i] == 1:
            codes[codes[i + 3]] = codes[codes[i + 1]] + codes[codes[i + 2]]
        elif codes[i] == 2:
            codes[codes[i + 3]] = codes[codes[i + 1]] * codes[codes[i + 2]]
    return codes[0]


if __name__ == "__main__":
    print(f"{main()}")
