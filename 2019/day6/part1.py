#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/6 - part 1


def get_input(file_path):
    p_map = {}
    with open(file_path) as f:
        for line in f:
            orb, center = tuple(reversed(line.strip().split(")")))
            p_map[orb] = center
    return p_map


def get_connections(orbits):
    cnt = 0
    for orbit in orbits:
        while True:
            center = orbits[orbit]
            cnt += 1
            if center == "COM":
                break
            orbit = center
    return cnt


def main():
    file_path = "input.txt"
    orbits = get_input(file_path)
    return get_connections(orbits)


if __name__ == "__main__":
    print(f"{main()}")
