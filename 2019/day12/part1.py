#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/12 - part 1

import re
from collections import defaultdict


def get_input(file_path):
    reg = re.compile('=(-?\d+)')
    with open(file_path) as f:
        return [get_coordinates(line, reg) for line in f]


def get_coordinates(line, reg):
    return tuple(int(coord) for coord in reg.findall(line))


def activate_gravity(planets, vec_planet_map):
    for i, planet_i in enumerate(planets):
        pl_i_vel_map = vec_planet_map[i]
        for planet_j in planets:
            if planet_i == planet_j:
                continue
            for coord_idx, (coord_i, coord_j) in enumerate(zip(planet_i, planet_j)):
                if coord_i < coord_j:
                    pl_i_vel_map[coord_idx] += 1
                elif coord_i > coord_j:
                    pl_i_vel_map[coord_idx] -= 1
        vec_planet_map[i] = pl_i_vel_map
    return vec_planet_map


def activate_velocity(planets, planet_velocity_map):
    for i, planet in enumerate(planets):
        vel_map = planet_velocity_map[i]
        planets[i] = tuple(coord + vel_map[idx] for idx, coord in enumerate(planet))
    return planets


def get_total_energy(planets, planet_velocity_map):
    energy = 0
    for i, planet in enumerate(planets):
        planet_vel = planet_velocity_map[i]
        pot_energy = sum(abs(coord) for coord in planet)
        kin_energy = sum(abs(vel) for vel in planet_vel.values())
        energy += pot_energy * kin_energy
    return energy


def main():
    input_file = 'input.txt'
    planets = get_input(input_file)
    planet_velocity_map = {i: defaultdict(int) for i, _ in enumerate(planets)}
    step = 0
    while True:
        planet_velocity_map = activate_gravity(planets, planet_velocity_map)
        planets = activate_velocity(planets, planet_velocity_map)
        step += 1
        if step == 1000:
            energy = get_total_energy(planets, planet_velocity_map)
            break
    return energy


if __name__ == "__main__":
    print(f"{main()}")
