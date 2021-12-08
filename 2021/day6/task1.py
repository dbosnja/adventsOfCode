#!/bin/python3


def get_input(file_path):
    with open(file_path) as f:
        return [int(c) for c in f.readline().strip().split(',')]


def main():
    file_path = 'input.txt'
    fish_state = get_input(file_path)
    for _ in range(80):
        for i, _ in enumerate(fish_state[:]):
            fish_state[i] -= 1
            if fish_state[i] < 0:
                fish_state[i] = 6
                fish_state.append(8)
    print(len(fish_state))


if __name__ == '__main__':
    main()