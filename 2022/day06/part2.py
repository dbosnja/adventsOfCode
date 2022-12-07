def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            return line.strip()


def main():
    in_file = 'input.txt'
    in_data = get_input(in_file)
    start = 0
    while True:
        if len(set(in_data[start: start + 14])) == 14:
            print(start + 14)
            break
        start += 1

main()