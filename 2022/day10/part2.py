def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            if 'noop' in line:
                yield line.strip(), 0
            else:
                opcode, scalar = line.strip().split()
                yield opcode, int(scalar)


def main():
    in_file = 'input.txt'
    x = 1
    cycle_cnt = 1
    bitmap = []
    for opcode, scalar in get_input(in_file):
        if opcode == 'noop':
            bitmap.append(x)
            cycle_cnt += 1
        else:
            bitmap.append(x)
            cycle_cnt += 1
            bitmap.append(x)
            x += scalar
            cycle_cnt += 1            
    
    bitmap = [bitmap[i * 40:(i + 1) * 40] for i in range(6)]
    for row in bitmap:
        for i, pix in enumerate(row):
            if i in [pix - 1, pix, pix + 1]:
                print('#', end='')
            else:
                print('.', end='')
        print()


main()