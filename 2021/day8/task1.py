#!/bin/python3


def get_input(file_path):
    outputs = []
    with open(file_path) as f:
        for line in f:
            outputs.extend(line.strip().split(' | ')[-1].split())
    return outputs



def main():
    file_path = 'input.txt'
    outputs = get_input(file_path)
    cnt = 0
    for digit in outputs:
        if len(digit) in (2, 3, 4, 7):
            cnt += 1
    print(cnt)



if __name__ == '__main__':
    main()