def get_input(in_file):
    with open(in_file) as f:
        for line in f:
            yield line.strip()


def get_dir_size(dir, file_system_map):
    total_sum = 0
    for i in file_system_map[dir]:
        if isinstance(i, int):
            total_sum += i
        else:
            total_sum += get_dir_size(i, file_system_map)
    return total_sum


def main():
    in_file = 'input.txt'
    file_system_map, dir_sizes_map = {}, {}
    cwd = ''
    total_sum = 0
    for line in get_input(in_file):
        if line.strip().startswith('$'):
            if 'cd' in line:
                dir_label = line.strip(' $').split()[-1]
                if dir_label == '/':
                    cwd = '/'
                else:
                    cwd = cwd + '%' + dir_label if dir_label != '..' else cwd.rsplit('%', 1)[0]
            else:
                file_system_map[cwd] = []
        else:
            if 'dir' in line:
                dir_label = line.split('dir')[-1].strip()
                file_system_map[cwd].append(cwd + '%' + dir_label)
            else:
                file_system_map[cwd].append(int(line.strip().split()[0]))
    for dir in file_system_map:
        dir_sizes_map[dir] = get_dir_size(dir, file_system_map)
    for size in dir_sizes_map.values():
        if size <= 100000:
            total_sum += size
    print(total_sum)


main()