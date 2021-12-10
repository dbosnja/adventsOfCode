#!/bin/python3

open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

closure_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def get_input(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()


def find_corrupt_char(line):
    buffer = []
    for c in line:
        if c in open_to_close:
            buffer.append(c)
        else:
            last_opened = buffer.pop()
            if open_to_close[last_opened] != c:
                return c
    return None


def main():
    file_path = 'input.txt'
    syntax_score = 0
    for line in get_input(file_path):
        illegal_char = find_corrupt_char(line)
        if illegal_char is None:
            continue
        syntax_score += closure_map[illegal_char]
    print(syntax_score)


if __name__ == '__main__':
    main()