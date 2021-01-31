#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/15#part2

from collections import defaultdict


def get_next_number(last_spoken_number, spoken_counter):
    """return next number to be spoken, according to rules(a)

    a) If last_spoken_number occured 0 or 1 time so far return 0,
       otherwise return distance between the positions of two last
       occurences of the number

    :param last_spoken_number: int
    :param spoken_counter: defaultdict(int)
    :rtype: int
    """
    positions = spoken_counter[last_spoken_number]
    if not positions or len(positions) == 1:
        # only one occurence so far
        return 0
    else:
        second_to_last_occ, last_occ = positions
        return last_occ - second_to_last_occ


def save_next_number(next_number, spoken_counter, turn_number):
    """save the position of the last spoken number

    :param next_number: the last spoken number
    :param spoken_counter: data record of spoken numbers
    :param turn_number: ordinal of the current spoken number
    :rtype: NoneType
    """
    positions = spoken_counter[next_number]
    positions.append(turn_number)
    if len(positions) in (1, 2):
        return
    # make sure only two elements always
    spoken_counter[next_number] = spoken_counter[next_number][1:]



def main():
    spoken_counter = defaultdict(list)
    # time's almost up! better hardcode them input
    spoken_counter[11].append(1)
    spoken_counter[0].append(2)
    spoken_counter[1].append(3)
    spoken_counter[10].append(4)
    spoken_counter[5].append(5)
    spoken_counter[19].append(6)
    turn_number = 6
    last_spoken_number = 19
    while True:
        turn_number += 1
        last_spoken_number = get_next_number(last_spoken_number, spoken_counter)
        save_next_number(last_spoken_number, spoken_counter, turn_number)
        if turn_number == 30000000: break
    return last_spoken_number


if __name__ == "__main__":
    print(f"resulting number: {main()}")
