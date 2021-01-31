#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/13 - part one
from functools import reduce


def find_me_first_bus(my_depart_time, busses_id):
    """find the (first bus, waiting time for it) tuple

    :rtype: tuple
    """
    # let's check first if there is one bus departing 
    # at the moment I'm ready to go; 
    # multiple matches are irrelevant - the result will be zero
    for bus_id in busses_id:
        if not my_depart_time % bus_id: return 0
    # otherwise let's check how much we need to wait for each bus
    bus_waiting_time_map = {}
    for bus_id in busses_id:
        bus_waiting_time_map[bus_id] = get_waiting_time(my_depart_time, bus_id)
    # let's find the bus with the minimum waiting time
    first_available_bus = sorted(bus_waiting_time_map,
                                 key=bus_waiting_time_map.get)[0]
    return first_available_bus, bus_waiting_time_map[first_available_bus]


def get_waiting_time(my_depart_time, bus_id):
    """calculate how much should I wait for this bus
    
    :rtype: int
    """
    return (my_depart_time // bus_id + 1) * bus_id - my_depart_time


with open('puzzle_input.txt') as f:
    my_depart_time = int(f.readline().strip())
    buses_depart_time = f.readline().strip()

if not my_depart_time:
    # if I'm ready at t=0, then the result is 0
    print(f"the solution is {my_depart_time}")

busses_id = [int(it) for it in buses_depart_time.split(',') if it != 'x']
result_time = reduce(lambda x, y: x*y, find_me_first_bus(my_depart_time, busses_id))
print(f"{result_time}")
