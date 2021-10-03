#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/6 - part 1

from collections import defaultdict


def get_input(file_path):
    p_map = {}
    with open(file_path) as f:
        for line in f:
            orb, center = tuple(reversed(line.strip().split(")")))
            p_map[orb] = center
    return p_map


def leave_trace(orbits, planet):
    trace = []
    while True:
        center = orbits[planet]
        trace.append(center)
        planet = center
        if center == "COM":
            break
    return trace


def get_center_to_orbits_map(input_file):
    with open(input_file) as f:
        planet_pairs = [line.strip().split(")") for line in f]
        c_o_map = defaultdict(set)
        for center, orbit in planet_pairs:
            c_o_map[center].add(orbit)
    return c_o_map


def get_mutual_planet(orbits, c_orbits_map, planet, my_trace):
    while True:
        center = orbits[planet]
        if any(mtr in c_orbits_map[center] for mtr in my_trace):
            return center
        # else, map yourself further
        planet = center


def main():
    file_path = "input.txt"
    orbits = get_input(file_path)
    my_planet = orbits["YOU"]
    santa_planet = orbits["SAN"]
    my_trace = leave_trace(orbits, my_planet)
    santa_trace = leave_trace(orbits, santa_planet)
    c_orbits_map = get_center_to_orbits_map(file_path)
    mt_planet = get_mutual_planet(orbits, c_orbits_map, santa_planet, my_trace)
    print(len(santa_trace))
    return my_trace.index(mt_planet) + 1 + santa_trace.index(mt_planet) + 1


if __name__ == "__main__":
    print(f"{main()}")
