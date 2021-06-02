#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/4 - part 1


def main(password_range):
    cnt = 0
    for pass_cand in range(password_range[0], password_range[1] + 1):
        if is_ascending(pass_cand) and contains_siblings(pass_cand):
            cnt += 1

    return cnt


def is_ascending(pass_cand):
    temp_digit = pass_cand % 10

    while pass_cand:
        pass_cand //= 10
        if pass_cand % 10 > temp_digit:
            return False
        temp_digit = pass_cand % 10

    return True

def contains_siblings(pass_cand):
    return any([x[0] == x[1] for x in slices([i for i in str(pass_cand)])])


def slices(a_list):
    temp_list = []
    for i, _ in enumerate(a_list):
        if i == len(a_list) - 1:
            break
        temp_list.append(a_list[i:i + 2])
    return temp_list


if __name__ == "__main__":
    password_range = [183564, 657474]
    print(main(password_range))
