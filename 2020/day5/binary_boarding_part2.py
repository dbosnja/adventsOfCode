#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/5 - part two


def get_seat_ids(file_path):
    """read input file & return a list of seat IDs
    
    :param file_path: path to input file
    :rtype: list
    """
    seat_ids = []
    with open(file_path) as f:
        for line in f:
            # if empty line, just continue
            if not line.strip(): continue
            seat_ids.append(get_seat_id(line.strip()))
    return seat_ids


def get_seat_id(line):
    """calculate the ID of a seat

    :param line: one non-empty line in input file
    :rtype: int
    """
    row_multiplier = 8
    seat_row = get_seat_row(line)
    seat_col = get_seat_col(line)
    return seat_row * row_multiplier + seat_col


def get_seat_row(line):
    """decode the cypher in the line and return the row of the seat

    :param line: one non-empty line in input file
    :rtype: int
    """
    first_row = 0
    last_row = 127
    for char in line:
        if char not in ('F', 'B'): return first_row
        elif char == "F":
            last_row = (first_row + last_row) // 2
        else:
            first_row = (first_row + last_row) // 2 + 1


def get_seat_col(line):
    """decode the cypher in the line and return the column of the seat

    :param line: one non-empty line in input file
    :rtype: int
    """
    first_col = 0
    last_col = 7
    for char in line:
        if char in ('F', 'B'): continue
        elif char == "L":
            last_col = (first_col + last_col) // 2
        else:
            first_col = (first_col + last_col) // 2 + 1
    # we can return either first_col or last_col
    return first_col

def find_my_boarding_pass_id(seat_ids):
    """return the missing ID from seat_ids
    
    :param seat_ids: sorted list of seat_ids
    :rtype: int
    """
    for i, seat_id in enumerate(seat_ids):
        if seat_ids[i + 1] - seat_id != 1: return seat_id + 1


def main():
    file_path = 'input.txt'
    seat_ids = get_seat_ids(file_path)
    my_id = find_my_boarding_pass_id(sorted(seat_ids))
    print(f"{my_id}")


if __name__ == "__main__":
    main()
