#! /usr/bin/python3.9

from day9_new import IntCodeComputer


def get_input(file_path):
    with open(file_path) as f:
        return f.readline().strip().split(',')


def get_blocks_count(values):
    tiles_pos = {}
    for idx in range(0, len(values), 3):
        x, y, tile_id = values[idx:idx + 3]
        if tile_id == 2:
            print(x, y, tile_id)
            tiles_pos[(x, y)] = tile_id
    return tiles_pos


def main():
    file_path = 'input.txt'
    opcodes = get_input(file_path)
    cpu = IntCodeComputer(opcodes)
    cpu.run()
    values = cpu.output
    values = [val for val in values[2::3] if val == 2]
    print(len(values))


if __name__ == "__main__":
    main()
