#! /usr/bin/python3


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


def fold(paper, instructions):
    for instr in instructions:
        direction, val = instr.split('=')
        val = int(val)
        if direction == 'y':
            rows_to_merge = [row for i, row in enumerate(paper) if i > val]
            for i, row in enumerate(rows_to_merge):
                row_destination = val - (i + 1)
                if row_destination < 0:
                    break
                for j, r in enumerate(row):
                    paper[row_destination][j] = r if r else paper[row_destination][j]
            tmp_paper = []
            for i, row in enumerate(paper[:]):
                if i < val:
                    tmp_paper.append(paper[i])
            paper = tmp_paper
        else:
            col_cnt = len(paper[0])
            cols_to_merge = []
            for j in range(val + 1, col_cnt):
                cols_to_merge.append([row[j] for row in paper])
            for j, col in enumerate(cols_to_merge):
                col_destination = val - (j + 1)
                if col_destination < 0:
                    break
                for i, c in enumerate(col):
                    paper[i][col_destination] = c if c else paper[i][col_destination]
            tmp_paper = []
            for row in paper:
                tmp_paper.append([c for j, c in enumerate(row) if j <= val])
            paper = tmp_paper
    return paper


def get_grid(dots):
    only_xs = [x for x, _ in dots]
    only_ys = [y for _, y in dots]
    grid = []
    for _ in range(min(only_ys), max(only_ys) + 1):
        col_data = [0 for _ in range(min(only_xs), max(only_xs) + 1)]
        grid.append(col_data)
    for x, y in dots:
        grid[y][x] = 1
    return grid


def print_code(paper):
    for row in paper:
        row_output = []
        for c in row:
            if c == 1:
                row_output.append('#')
            else:
                row_output.append('.')
        print(''.join(row_output))


def main():
    file_path = 'input.txt'
    dots, instructions = get_input(file_path)
    paper = get_grid(dots)
    paper = fold(paper, instructions)
    print_code(paper)


if __name__ == '__main__':
    main()