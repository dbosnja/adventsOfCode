#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/13 - part two


def get_puzzle_input(file_path):
    """get given bus IDs in the file at 2nd line

    :param file_path: str
    :rtype: list
    """
    with open(file_path) as f:
        for line_no, line in enumerate(f):
            if not line_no: continue
            return line.strip()


def is_right_moment(time, bus_ids):
    """return True if the moment 'is the right one'

    :param time: a moment in some reality, step is alway 1(min); starts with 0
    :param bus_ids: list of bus_ids available in service
    :rtype: bool
    """
    for i, bus_id in enumerate(bus_ids):
        if bus_id == 'x': continue
        # otherwise let's check if bus_id fits the requirement at given time
        if not is_complied_bus_id(time, i, bus_ids): return False
    # all bus_ids comply to the given requirements
    return True


def is_complied_bus_id(time, i, bus_ids):
    """return True if bus_ids[i] departs at offset in time

    :param time: a moment in some reality, step is alway 1(min); starts with 0
    :param i: represents offset --> int
    :param bus_ids: list of bus_ids available in service
    :rtype: bool
    """
    return (time + i) % bus_ids[i] == 0


def main():
    file_path = 'puzzle_input.txt'
    bus_ids = list(map(lambda x: int(x) if x != "x" else x,
                  get_puzzle_input(file_path).split(",")))
    # let's say that probability of this happening - not likely at smaller numbers
    # still probability of it happening overall sometimes is 1?
    time_step = 0
    while True:
        time = time_step * 29
        if is_right_moment(time, bus_ids): return time
        time_step += 1
        print(f"time is: {time:0.5e}\n")


if __name__ == "__main__":
    # for given input, this program takes around 32 years to execute
    resulting_time = main()
    print(f"{resulting_time}")
