#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/3 - part two
from fractions import Fraction
from functools import reduce


def get_input_matrix(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f]


def extend_matrix(matrix, slope):
    """extend matrix so that with given slope we have enough 'side-hill'
       while 'down-hilling'
    
    :param matrix: list of lists; representing down hill toboggan trajectory
    :param slope: represents the slope of the trajectory we're taking. --> Fraction
    :rtype: list
    """
    # let's save number of rows and columns
    row_no, col_no = len(matrix), len(matrix[0])
    extended_matrix = []
    number_of_extensions = (row_no * slope.denominator + 1) // col_no + 1
    for row in matrix:    
        extended_row = []
        for _ in range(number_of_extensions):
            extended_row.extend(row)
        extended_matrix.append(extended_row)
    return extended_matrix


def get_number_of_trees(extended_matrix, slope):
    """return number of trees hit while skiing down-hill on the
       toboggan trajectory

    :param: list of lists
    :param slope: represents the slope of the trajectory we're taking. --> Fraction
    :rtype: int
    """
    start_i, start_j = 0, 0
    number_of_trees = 0
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
    input_matrix = get_input_matrix(file_path)
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    outcome_by_slope = []
    for numerator, denominator in slopes:
        slope = Fraction(numerator, denominator)
        extended_matrix = extend_matrix(input_matrix, slope)
        outcome_by_slope.append(get_number_of_trees(extended_matrix, slope))
    return reduce(lambda x, y: x*y, outcome_by_slope)
    

if __name__ == "__main__":
    optmized_trajectory = main()
    print(f"{optmized_trajectory}")
