#!/bin/python3

def get_input(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]


def main():
    file_path = 'input.txt'
    values = get_input(file_path)
    cnt = 0
    for i, val in enumerate(values[:-1]):
        if val < values[i + 1]:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()