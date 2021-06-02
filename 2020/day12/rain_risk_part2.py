#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/12#part2

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


def move_the_trajectory(action, value, trajectory_map):
    """move and return new location of the waypoint or the ship

    :param action: tells the side of the world --> str
    :param value: tells the value of the action --> int
    :param trajectory_map: current location of the waypoint
    :rtype: defaultdict(int)
    """
    action_pairs = [["N", "S"], ["E", "W"]]
    for action_pair in action_pairs:
        if action in action_pair:
            connection = action_pair
            break
    connection.remove(action)
    cntr_action = connection.pop()
    temp_value = trajectory_map[action] + value - trajectory_map[cntr_action]
    if temp_value < 0:
        trajectory_map[cntr_action] = temp_value
    else:
        trajectory_map[action] = temp_value
    return trajectory_map


def forward_the_ship(value, waypoint_map, ship_map):
    """forward the ship toward the waypoint_map and it also

    :param value: tells the value of the action --> int
    :param waypoint_map: current location of the waypoint
    :param ship_map: current location of the ship
    :rtype: defaultdict(int)
    """
    for key, value in waypoint_map.items():
        ship_map = move_the_trajectory(key, value, ship_map)
    return ship_map



def main():
    file_path = "input.txt"
    ship_instructions = get_ship_instructions(file_path)
    ship_trajectory_map = defaultdict(int)
    waypoint_trajectory_map = defaultdict(int)
    # by default starting location of the waypoint is
    waypoint_trajectory_map['N'] += 1
    waypoint_trajectory_map['E'] += 10
    for action, value in ship_instructions:
        if action in ('E', 'W', 'N', 'S',):
            waypoint_trajectory_map = move_the_trajectory(action,
                                        value, waypoint_trajectory_map)
        elif action in ('F'):
            ship_trajectory_map = forward_the_ship(value,
             waypoint_trajectory_map, ship_trajectory_map)
        # else the ship is changing its direction!
        else:
            direction = get_new_direction(direction, action, value)


if __name__ == "__main__":
    main()
