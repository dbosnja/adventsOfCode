#! /usr/bin/python3

from collections import defaultdict


def get_input(file_path):
    dots = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                instructions = [ln.strip().replace('fold along ', '') for ln in f.readlines()]
                break
            dots.append([int(c) for c in line.strip().split(',')])
    return dots, instructions


def get_row_col_map(dots):
    row_map, col_map = defaultdict(set), defaultdict(set)
    for x, y in sorted(dots, key=lambda X: X[1]):
        row_map[y].add(x)
    for x, y in sorted(dots, key=lambda X: X[0]):
        col_map[x].add(y)
    return row_map, col_map


def fold(instructions, row_map, col_map):
    for instr in instructions:
        direction, val = instr.split('=')
        val = int(val)
        if direction == 'y':
            rows_to_map = [r for r in row_map if r > val]
            for row in rows_to_map:
                row_to_be_merged = val - (row - val)
                if row_to_be_merged < 0:
                    break
                row_map[row_to_be_merged] = row_map[row_to_be_merged].union(row_map[row])
            for row in list(row_map.keys()):
                if row >= val:
                    row_map.pop(row)
            for rows in col_map.values():
                if val in rows:
                    rows.remove(val)
        elif direction == 'x':
            col_to_map = [c for c in col_map if c > val]
            for col in col_to_map:
                col_to_be_merged = val - (col - val)
                if col_to_be_merged < 0:
                    break
                col_map[col_to_be_merged] = col_map[col_to_be_merged].union(col_map[col])
            for col in list(col_map.keys()):
                if col >= val:
                    col_map.pop(col)
            for cols in row_map.values():
                if val in cols:
                    cols.remove(val)
        break
    return row_map, col_map


def main():
    file_path = 'input.txt'
    dots, instructions = get_input(file_path)
    row_map, col_map = get_row_col_map(dots)
    row_map, col_map = fold(instructions, row_map, col_map)
    print(sum(len(rows) for rows in col_map.values()))


if __name__ == '__main__':
    main()