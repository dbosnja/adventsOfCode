direction_map = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            direction, scalar = line.strip().split()
            yield direction_map[direction], int(scalar)


def is_adjacent(tail_pos, head_pos):
    if tail_pos == head_pos: return True
    if tail_pos[0] == head_pos[0]:
        return abs(tail_pos[1] - head_pos[1]) == 1
    if tail_pos[1] == head_pos[1]:
        return abs(tail_pos[0] - head_pos[0]) == 1
    return abs(tail_pos[0] - head_pos[0]) == 1 and abs(tail_pos[1] - head_pos[1]) == 1


def main():
    in_file = 'input.txt'
    tail_trajectory = set()
    tail_trajectory.add((0, 0))
    head_pos, tail_pos = (0, 0), (0, 0)
    for dir_vector, scalar in get_input(in_file):
        for _ in range(scalar):
            head_pos = head_pos[0] + dir_vector[0], head_pos[1] + dir_vector[1]
            if is_adjacent(tail_pos, head_pos): continue
            if tail_pos[0] == head_pos[0] or tail_pos[1] == head_pos[1]:
                tail_pos = tail_pos[0] + dir_vector[0], tail_pos[1] + dir_vector[1]
                tail_trajectory.add(tail_pos)
            else:
                if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
                    tail_pos = tail_pos[0] + 1, tail_pos[1] + 1
                elif head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
                    tail_pos = tail_pos[0] - 1, tail_pos[1] + 1
                elif head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
                    tail_pos = tail_pos[0] - 1, tail_pos[1] - 1
                elif head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]:
                    tail_pos = tail_pos[0] + 1, tail_pos[1] - 1
                tail_trajectory.add(tail_pos)     
    
    print(len(tail_trajectory))


main()