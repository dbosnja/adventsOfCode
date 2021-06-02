#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/11#part2
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
from math import sin, cos, radians
from time import time


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
    """apply fill_the_seat rule(a) to a seat(b).

       a) if there are no occupied seats in all
          8 directions of the seat, occupy this seat
       b) seat is defined as an element of the matrix ie equals to: seats[i][j]

    :param i: current row of the seat --> int
    :param j: current column of the seat --> int
    :param seats: matrix of seats --> list
    :rtype: str
    """
    occupied_sign = "#"
    floor_sign = "."
    seats_around = set()
    number_of_directions = 8
    # we're making a "full circle"
    full_circle = 360
    # density of the discretization grid
    angle = full_circle // number_of_directions
    # iterate over all 8 directions
    for angle_pie in range(0, full_circle, angle):
        original_slope = get_direction(angle_pie)
        # scalar for extending direction
        slope_scalar = 0
        while True:
            slope_scalar += 1
            # let's go along the slope direction
            slope = (i + slope_scalar * original_slope[0],
                    j + slope_scalar * original_slope[1])
            if not (0 <= slope[0] <= len(seats) - 1) or \
               not (0 <= slope[1] <= len(seats[0]) - 1):
                # we're out of the operator's domain
                break
            if seats[slope[0]][slope[1]] == floor_sign:
                # nothing do to here, extend the direction
                continue
            seats_around.add(seats[slope[0]][slope[1]])
            break

    if occupied_sign not in seats_around:
        return occupied_sign
    # the seat remain the same state if the requirement not satisfied
    return identity(i, j, seats)


def free_the_seat(i, j, seats):
    """apply free_the_seat(a) rule to a seat(b).

       a) if there are 5 or more occupied seats in all 8
          directions combined, empty this seat
       b) seat=seats[i][j]

    :param i: current row of the seat --> int
    :param j: current column of the seat --> int
    :param seats: matrix of seats --> list
    :rtype: str
    """
    occupied_sign = "#"
    empty_sign = "L"
    floor_sign = "."
    seats_around = []
    number_to_free_seat = 5
    number_of_directions = 8
    # we're making a "full circle"
    full_circle = 360
    # density of the discretization grid
    angle = full_circle // number_of_directions
    for angle_pie in range(0, full_circle, angle):
        original_slope = get_direction(angle_pie)
        # scalar for extending direction
        slope_scalar = 0
        while True:
            slope_scalar += 1
            # let's go along the slope direction
            slope = (i + slope_scalar * original_slope[0],
                     j + slope_scalar * original_slope[1])
            if not (0 <= slope[0] <= len(seats) - 1) or \
               not (0 <= slope[1] <= len(seats[0]) - 1):
                # we're out of the operator's domain
                break
            if seats[slope[0]][slope[1]] == floor_sign:
                # nothing do to here, extend the direction
                continue
            seats_around.append(seats[slope[0]][slope[1]])
            break

    if seats_around.count(occupied_sign) >= number_to_free_seat:
        return empty_sign
    # the seat remain the same state if the requirement not satisfied
    return identity(i, j, seats)


def get_direction(angle):
    """return a dot on a circle with radius 1

    :param angle: angle in degrees --> int
    :rtype: tuple
    """
    radian_angle = radians(angle)
    slope = tuple(map(round, (sin(radian_angle), cos(radian_angle))))
    return (-slope[0], slope[1])


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
    step = 1
    while seats != updated_seats:
        start_time = time()
        step += 1
        seats = updated_seats
        updated_seats = update_seats(seats)
        print(f"current step: {step}")
        end_time = time() - start_time
        print(f"its running time: {end_time: 0.4}s")
        print('\n')
    return count_occupied(seats)


if __name__ == "__main__":
    occupied_seats = main()
    print(f"{occupied_seats}")
