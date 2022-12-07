import re

from collections import defaultdict

def get_input(in_file):
    rows = []
    crane_stack_map = defaultdict(list)
    re_pat = '(\s{3}|\[\w{1}\]){1}\s{1}'
    re_cmp = re.compile(re_pat)
    re_pat_instruction = '(\d+)'
    re_cmp_instruction = re.compile(re_pat_instruction)
    with open(in_file) as f:
        for line in f:
            if line.strip().startswith('1'):
                break
            rows.append(re_cmp.findall(line))
        for row in rows:
            for i, crane in enumerate(row):
                if not crane.strip(): continue
                crane = crane.strip().strip('[]')
                crane_stack_map[i + 1].append(crane)
        for key, val in crane_stack_map.items():
            crane_stack_map[key] = list(reversed(val))
        yield crane_stack_map
        for line in f:
            if not line.strip(): continue
            yield [int(i) for i in re_cmp_instruction.findall(line.strip())]


def main():
    in_file = 'input.txt'
    input_gen = get_input(in_file)
    crane_stack_map = next(input_gen)
    for instr in input_gen:
        cnt = instr[0]
        crane_stack_map[instr[2]].extend(crane_stack_map[instr[1]][-cnt:])    
        crane_stack_map[instr[1]] = crane_stack_map[instr[1]][:-cnt]        
    print(''.join([crane_stack_map[i].pop() for i in range(1, 10)]))


main()