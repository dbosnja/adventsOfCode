#!/bin/python3

open_to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

closure_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def get_input(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()


def find_incomplete_chars(line):
    buffer = []
    for c in line:
        if c in open_to_close:
            buffer.append(c)
        else:
            last_opened = buffer.pop()
            if open_to_close[last_opened] != c:
                return None
    assert len(buffer) != 0
    return reversed(buffer)


def main():
    file_path = 'input.txt'
    syntax_scores = []
    for line in get_input(file_path):
        tmp_sum = 0
        illegal_chars = find_incomplete_chars(line)
        if illegal_chars is None:
            continue
        for c in illegal_chars:
            tmp_sum = 5 * tmp_sum + closure_map[open_to_close[c]]
        syntax_scores.append(tmp_sum)
    syntax_scores.sort()
    middle = len(syntax_scores) // 2
    print(syntax_scores[middle])


if __name__ == '__main__':
    main()