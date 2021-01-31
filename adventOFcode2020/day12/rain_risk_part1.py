#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/12 - part 1

import re
from functools import namedtuple
from collections import defaultdict

ship_instruction = namedtuple("ship_instruction", ["action", "value"])


def get_ship_instructions(file_path):
    """read input file and return the ship instruction where to sail

    :param file_path: file path to input file --> str
    :rtype: list
    """
    ship_instructions = []
    with open(file_path) as f:
        for line in f:
            value = re.search(r"\d+", line.strip()).group().strip()
            action = line.replace(value, "").strip()
            ship_instructions.append(ship_instruction(action, int(value)))
    return ship_instructions


def get_new_direction(direction, action, value):
    """return new direction of the ship based on action(left or right)
       and take turn for value degrees

    :param direction: current direction of the ship
    :param action: this is going to be either 'L' or 'R'
    :param value: represents how much for ship to move --> int
    :rtype: str
    """
    world_side_to_number = {
        'E': 0,
        'N': 1,
        'W': 2,
        'S': 3,
    }
    # let's first check if the number of degrees is too big:
    if value >= 360:
        value = value % 360
    number_of_turns = value // 90
    if action == "L":
        side = (world_side_to_number[direction] + number_of_turns) % 4
        for it, val in world_side_to_number.items():
            if val == side: return it
    elif action == "R":
        side = (world_side_to_number[direction] - number_of_turns) % 4
        for it, val in world_side_to_number.items():
            if val == side: return it

def main():
    file_path = "input.txt"
    ship_instructions = get_ship_instructions(file_path)
    trajectory_map = defaultdict(int)
    # by default starting direction of the ship is East
    direction = 'E'
    for action, value in ship_instructions:
        if action in ('E', 'W', 'N', 'S',):
            trajectory_map[action] += value
        elif action in ('F'):
            trajectory_map[direction] += value
        # else the ship is changing its direction!
        else:
            direction = get_new_direction(direction, action, value)
    east_west_distance = abs(trajectory_map['W'] - trajectory_map['E'])
    north_south_distance = abs(trajectory_map['S'] - trajectory_map['N'])
    print(east_west_distance + north_south_distance)


if __name__ == "__main__":
    main()
