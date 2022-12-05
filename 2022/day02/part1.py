game_rules = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            yield line.strip().split()



def main():
    in_file = 'input.txt'
    my_choices_map = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    total_sum = 0
    for left, rigth in get_input(in_file):
        total_sum += game_rules[(left, rigth)] + my_choices_map[rigth]
    print(total_sum)

main()