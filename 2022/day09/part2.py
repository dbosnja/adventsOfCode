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


def make_adjacent(head_pos, snake, dir_vector):
    new_snake = []
    temp_pos = head_pos
    for i, pos in enumerate(snake):
        if is_adjacent(temp_pos, pos):
            new_snake.append(pos)
            temp_pos = pos
            continue
        if temp_pos[0] == pos[0]:
            y = pos[1] + 1 if temp_pos[1] > pos[1] else pos[1] - 1
            pos = pos[0], y
        elif temp_pos[1] == pos[1]:
            x = pos[0] + 1 if temp_pos[0] > pos[0] else pos[0] - 1
            pos = x, pos[1]
        else:
            if temp_pos[0] > pos[0] and temp_pos[1] > pos[1]:
                pos = pos[0] + 1, pos[1] + 1
            elif temp_pos[0] < pos[0] and temp_pos[1] > pos[1]:
                pos = pos[0] - 1, pos[1] + 1
            elif temp_pos[0] < pos[0] and temp_pos[1] < pos[1]:
                pos = pos[0] - 1, pos[1] - 1
            elif temp_pos[0] > pos[0] and temp_pos[1] < pos[1]:
                pos = pos[0] + 1, pos[1] - 1
        new_snake.append(pos)
        temp_pos = pos
    return new_snake


def main():
    in_file = 'input.txt'
    tail_trajectory = set()
    tail_trajectory.add((0, 0))
    head_pos = (0, 0)
    snake = [(0, 0) for _ in range(9)]
    for dir_vector, scalar in get_input(in_file):
        for _ in range(scalar):
            head_pos = head_pos[0] + dir_vector[0], head_pos[1] + dir_vector[1]
            snake = make_adjacent(head_pos, snake, dir_vector)
            tail_trajectory.add(snake[-1])
    print(len(tail_trajectory))


main()