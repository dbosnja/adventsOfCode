from math import prod


def get_input(in_file):
    tree_grid = []
    with open(in_file) as f:
        for line in f:
            tree_grid.append([int(i) for i in line.strip()])
    return tree_grid


def get_scenic_score(i, j, tree_grid):
    row_cnt, col_cnt = len(tree_grid), len(tree_grid[0])
    sums = []
    total_sum = 0
    for k in range(j - 1, -1, -1):
        if tree_grid[i][k] >= tree_grid[i][j]:
            total_sum += 1
            break
        else:
            total_sum += 1
    sums.append(total_sum)
    
    total_sum = 0
    for k in range(j + 1, col_cnt):
        if tree_grid[i][k] >= tree_grid[i][j]:
            total_sum += 1
            break
        else:
            total_sum += 1
    sums.append(total_sum)
    
    total_sum = 0
    for k in range(i - 1, -1, -1):
        if tree_grid[k][j] >= tree_grid[i][j]:
            total_sum += 1
            break
        else:
            total_sum += 1
    sums.append(total_sum)
    
    total_sum = 0
    for k in range(i + 1, row_cnt):
        if tree_grid[k][j] >= tree_grid[i][j]:
            total_sum += 1
            break
        else:
            total_sum += 1
    sums.append(total_sum)
    
    return prod(sums)


def main():
    in_file = 'input.txt'
    tree_grid = get_input(in_file)
    row_cnt, col_cnt = len(tree_grid), len(tree_grid[0])
    max_scenic_score = 0
    for i in range(row_cnt):
        for j in range(col_cnt):
            i_j_scenic_score = get_scenic_score(i, j, tree_grid)
            if i_j_scenic_score > max_scenic_score:
                max_scenic_score = i_j_scenic_score
    print(max_scenic_score)


main()