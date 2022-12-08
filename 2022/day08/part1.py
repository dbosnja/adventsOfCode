def get_input(in_file):
    tree_grid = []
    with open(in_file) as f:
        for line in f:
            tree_grid.append([int(i) for i in line.strip()])
    return tree_grid


def count_if_visible(i, j, tree_grid):
    row_cnt, col_cnt = len(tree_grid), len(tree_grid[0])
    tree_candidates = []
    for k in range(j):
        tree_candidates.append(tree_grid[i][k] < tree_grid[i][j])
    if all(tree_candidates): return 1
    tree_candidates = []

    for k in range(j + 1, col_cnt):
        tree_candidates.append(tree_grid[i][k] < tree_grid[i][j])
    if all(tree_candidates): return 1
    tree_candidates = []

    for k in range(i):
        tree_candidates.append(tree_grid[k][j] < tree_grid[i][j])
    if all(tree_candidates): return 1
    tree_candidates = []

    for k in range(i + 1, row_cnt):
        tree_candidates.append(tree_grid[k][j] < tree_grid[i][j])
    if all(tree_candidates): return 1
    return 0


def main():
    in_file = 'input.txt'
    tree_grid = get_input(in_file)
    row_cnt, col_cnt = len(tree_grid), len(tree_grid[0])
    total_sum = 0
    for i in range(1, row_cnt - 1):
        for j in range(1, col_cnt - 1):
            total_sum += count_if_visible(i, j, tree_grid)
    total_sum += 2 * col_cnt + 2 * (row_cnt - 2)
    print(total_sum)


main()