#!/bin/python3

from collections import defaultdict


def get_input(file_path):
    fish_state = defaultdict(int)
    with open(file_path) as f:
        for i in [int(c) for c in f.readline().strip().split(',')]:
            fish_state[i] += 1
    return fish_state


def main():
    file_path = 'input.txt'
    fish_state = get_input(file_path)
    for _ in range(256):
        old_state = fish_state
        fish_state = defaultdict(int)
        for state, cnt in sorted(old_state.items()):
            if state == 0:
                fish_state[8] = cnt
                fish_state[6] = cnt
            elif state == 7:
                fish_state[6] += cnt
            else:
                fish_state[state - 1] = cnt
    print(sum(fish_state.values()))


if __name__ == '__main__':
    main()