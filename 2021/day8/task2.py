#!/bin/python3

digit_to_label = {
    0: frozenset('abcefg'),
    1: frozenset('cf'),
    2: frozenset('acdeg'),
    3: frozenset('acdfg'),
    4: frozenset('bcdf'),
    5: frozenset('abdfg'),
    6: frozenset('abdefg'),
    7: frozenset('acf'),
    8: frozenset('abcdefg'),
    9: frozenset('abcdfg'),
}

label_to_digit = {v: k for k, v in digit_to_label.items()}


def get_input(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()


def get_premliminaries(equations):
    pairs_map = {}
    len_2_eq = [e for e in equations if len(e) == 2].pop()
    len_3_eq = [e for e in equations if len(e) == 3].pop()
    len_4_eq = [e for e in equations if len(e) == 4].pop()
    pairs_map[frozenset(len_2_eq)] = digit_to_label[1]
    len_4_eq = frozenset(len_4_eq) - frozenset(len_2_eq)
    pairs_map[len_4_eq] = digit_to_label[4] - digit_to_label[1]
    len_3_eq = (set(len_3_eq) - set(len_2_eq)).pop()
    len_3_val = set(digit_to_label[7] - digit_to_label[1]).pop()
    return len_3_eq, len_3_val, pairs_map


def get_double_eq(equations, pairs_map):
    doubles_len5 = [e for e in equations if len(e) == 5]
    doubles_len6 = [e for e in equations if len(e) == 6]
    p1, p2 = pairs_map.keys()
    tmp_set = {d for d in doubles_len5 if set(p1).issubset(set(d)) or set(p2).issubset(set(d))}
    doubles_len5 = list(tmp_set) + list(set(doubles_len5) - tmp_set)
    tmp_set = {d for d in doubles_len6 if set(p1).issubset(set(d)) or set(p2).issubset(set(d))}
    doubles_len6 = list(tmp_set) + list(set(doubles_len6) - tmp_set)
    return doubles_len5 + doubles_len6


def filter_uniques(eq, label, unique_digit_to_label):
    eq, label = [set(i) for i in (eq, label)]
    for new, old in unique_digit_to_label.items():
        if new not in eq:
            continue
        if old not in label:
            return None, None
        # it is inside, filter eq and label
        eq.remove(new)
        label.remove(old)
    return eq, label


def filter_pairs(eq, label, pairs_map):
    eq, label = [set(i) for i in (eq, label)]
    for new, old in pairs_map.items():
        if not set(new).issubset(eq):
            continue
        if not set(old).issubset(label):
            return None, None
        # it is inside, filter eq and label
        eq -= set(new)
        label -= set(old)
    return eq, label


def filter_per_point(eq, label, pairs_map):
    eq, label = [set(i) for i in (eq, label)]
    for new, old in pairs_map.items():
        for point in new:
            if point not in eq:
                continue
            if not any(p in label for p in old):
                return None, None
            for p in old:
                if p in label:
                    label.remove(p)
                    eq.remove(point)
                    break
    return eq, label


def update_pairs_map(unique_digit_to_label, pairs_map):
    discarded_pairs = []
    for pair in pairs_map:
        p1, p2 = pair
        if p1 in unique_digit_to_label:
            val1 = unique_digit_to_label[p1]
            val2 = set(pairs_map[pair])
            val2.remove(val1)
            assert len(val2) == 1
            unique_digit_to_label[p2] = val2.pop()
            discarded_pairs.append(pair)
        elif p2 in unique_digit_to_label:
            val2 = unique_digit_to_label[p2]
            val1 = set(pairs_map[pair])
            val1.remove(val2)
            assert len(val1) == 1
            unique_digit_to_label[p1] = val1.pop()
            discarded_pairs.append(pair)
    return {k: pairs_map[k] for k in pairs_map if k not in discarded_pairs}


def decode_last_char(unique_digit_to_label):
    if len(unique_digit_to_label) == 7:
        return None
    k = (set(digit_to_label[8]) - set(unique_digit_to_label)).pop()
    v = (set(digit_to_label[8]) - set(unique_digit_to_label.values())).pop()
    unique_digit_to_label[k] = v


def decode_output(outputs, unique_digit_to_label):
    decoded_ouputs = []
    for out in outputs:
        decoded = frozenset(''.join(unique_digit_to_label[c] for c in out))
        decoded_ouputs.append(str(label_to_digit[decoded]))
    return int(''.join(decoded_ouputs))


def main():
    file_path = 'input.txt'
    decoded_outputs = []
    for line in get_input(file_path):
        unique_digit_to_label = {}
        equations, outputs = [x.split() for x in line.split(' | ')]
        uniq_l, uniq_r, pairs_map = get_premliminaries(equations)
        unique_digit_to_label[uniq_l] = uniq_r
        for eq in get_double_eq(equations, pairs_map):
            if len(unique_digit_to_label) in (6, 7):
                break
            tmp_eq = set(eq)
            if len(eq) == 5:
                represents = (2, 3, 5)
            else:
                represents = (0, 6, 9)
            for i in represents:
                eq = tmp_eq
                label = digit_to_label[i]
                eq, label = filter_uniques(eq, label, unique_digit_to_label)
                if eq is label is None or eq == label == set():
                    continue
                eq, label = filter_pairs(eq, label, pairs_map)
                if eq is label is None or eq == label == set():
                    continue
                if len(eq) == len(label) == 1:
                    # new char decoded
                    unique_digit_to_label[eq.pop()] = label.pop()
                    pairs_map = update_pairs_map(unique_digit_to_label, pairs_map)
                    break
                eq, label = filter_per_point(eq, label, pairs_map)
                if eq is label is None or eq == label == set():
                    continue
                if len(eq) == len(label) == 1:
                    # new char decoder
                    unique_digit_to_label[eq.pop()] = label.pop()
                    pairs_map = update_pairs_map(unique_digit_to_label, pairs_map)
                    break
        decode_last_char(unique_digit_to_label)
        decoded_outputs.append(decode_output(outputs, unique_digit_to_label))
    print(sum(decoded_outputs))


if __name__ == '__main__':
    main()