game_rules = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',
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
    game_round_map = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    total_sum = 0
    for left, rigth in get_input(in_file):
        total_sum += my_choices_map[game_rules[(left, rigth)]] + game_round_map[rigth]
    print(total_sum)

main()