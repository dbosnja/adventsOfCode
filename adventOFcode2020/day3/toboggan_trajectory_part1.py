#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/3 - part one
from fractions import Fraction


def get_input_matrix(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]


def extend_matrix(matrix):
    """extend matrix so that with given slope we have enough 'side-hill'
       while 'down-hilling'
    
    :param matrix: list of lists; representing down hill toboggan trajectory
    :rtype: list
    """
    # let's save number of rows and columns
    row_no, col_no = len(matrix), len(matrix[0])
    slope = Fraction(1, 3)
    extend_matrix = []
    number_of_extensions = (row_no * slope.denominator + 1) // col_no + 1
    for row in matrix:    
        extended_row = []
        for _ in range(number_of_extensions):
            extended_row.extend(row)
        extend_matrix.append(extended_row)
    return extend_matrix


def get_number_of_trees(extended_matrix):
    """return number of trees hit while skiing down-hill on the
       toboggan trajectory

    :param: list of lists
    :rtype: int
    """
    start_i, start_j = 0, 0
    number_of_trees = 0
    slope = Fraction(1, 3)
    while True:
        # end of the toboggan party
        if start_i == len(extended_matrix) - 1:
            return number_of_trees
        # if not, go down-hill by given slope
        start_j += slope.denominator
        start_i += slope.numerator
        if extended_matrix[start_i][start_j] == "#": number_of_trees += 1


def main():
    file_path = "input.txt"
    extended_matrix = extend_matrix(get_input_matrix(file_path))
    return get_number_of_trees(extended_matrix)
    

if __name__ == "__main__":
    number_of_trees = main()
    print(f"{number_of_trees}")
