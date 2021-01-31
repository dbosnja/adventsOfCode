#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/11 - part 1
#
#
##################################################
#
# explanation behind this task should be behind the so called
# "idempotent operators"(for example in linear algebra)
# see for more:
# https://en.wikipedia.org/wiki/Idempotence
#
##################################################
#
#

from copy import deepcopy


def get_seats(file_path):
    """read input file and return a matrix of seats in
       the waiting area to board the ferry

    :param file_path: file path to input file --> str
    :rtype: list
    """
    seats = []
    with open(file_path) as f:
        for line in f:
            row = [seat for seat in line.strip()]
            seats.append(row)
    return seats


def update_seats(seats):
    """update the seats according to modelling rules
       'L' char represents an empty seat
       '#' char represents an occupied seat
       '.' char represents floor; never changes ie 'invariant' of modelling rules
       seats don't move and nobody seats on the floor

    :param seats: matrix of seats --> list
    :rtype: list
    """
    # simulates a dot-like matrix operator
    matrix_operator = {
        ".": identity,
        "L": fill_the_seat,
        "#": free_the_seat,
    }
    updated_seats = deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            updated_seats[i][j] = matrix_operator[seat](i, j, seats)
    return updated_seats


def identity(i, j, seats):
    """apply identity rule to a seat. (seat=seats[i][j])

    :param i: current row of the seat --> int
    :param j: current column of the seat --> int
    :param seats: matrix of seats --> list
    :rtype: str
    """
    return seats[i][j]


def fill_the_seat(i, j, seats):
    """apply fill_the_seat rule to a seat. (seat=seats[i][j])
       if there are no occupied adjacent seats to the seat,
       fill this seat

    :param i: current row of the seat --> int
    :param j: current column of the seat --> int
    :param seats: matrix of seats --> list
    :rtype: str
    """
    occupied_sign = "#"
    adjacent_seats = set()
    # if possible, let's make the smallest square around this seat
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if i + x_offset not in range(len(seats)) or \
                j + y_offset not in range(len(seats[0])) or \
                not (x_offset or y_offset):
                # we're out of the operator's domain or
                # in the middle of the square
                continue
            adjacent_seats.add(seats[i + x_offset][j + y_offset])
    if occupied_sign not in adjacent_seats:
        return occupied_sign
    return seats[i][j]


def free_the_seat(i, j, seats):
    """apply free_the_seat rule to a seat. (seat=seats[i][j])
       if there are 4 or more occupied adjacent seats to the seat,
       empty this seat

    :param i: current row of the seat --> int
    :param j: current column of the seat --> int
    :param seats: matrix of seats --> list
    :rtype: str
    """
    occupied_sign = "#"
    empty_sign = "L"
    adjacent_seats = []
    number_to_free_seat = 4
    # if possible, let's make the smallest square around this seat
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if i + x_offset not in range(len(seats)) or \
                j + y_offset not in range(len(seats[0])) or \
                not (x_offset or y_offset):
                # we're out of the operator's domain or
                # in the middle of the square
                continue
            adjacent_seats.append(seats[i + x_offset][j + y_offset])
    if adjacent_seats.count(occupied_sign) >= number_to_free_seat:
        return empty_sign
    return seats[i][j]


def count_occupied(seats):
    """count number of occupied('#') seats in the matrix

    :param seats: matrix of seats --> list
    :rtype: int
    """
    occupied_sign = "#"
    occupied_sum = 0
    for row in seats:
        for seat in row:
            if seat == occupied_sign:
                occupied_sum += 1
    return occupied_sum


def main():
    file_path = "input.txt"
    seats = get_seats(file_path)
    # apply matrix_operator on seats
    updated_seats = update_seats(seats)
    while seats != updated_seats:
        seats = updated_seats
        updated_seats = update_seats(seats)
    return count_occupied(seats)


if __name__ == "__main__":
    occupied_seats = main()
    print(f"{occupied_seats}")
