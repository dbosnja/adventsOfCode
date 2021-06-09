#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/4 - part 2


def main(password_range):
    cnt = 0
    for pass_cand in range(password_range[0], password_range[1] + 1):
        if is_ascending(pass_cand) and contains_siblings(pass_cand):
            cnt += 1

    return cnt


def is_ascending(pass_cand):
    pass_cand = str(pass_cand)
    if any(pass_cand[i] > pass_cand[i+1] for i in range(len(pass_cand) - 1)):
        return False
    return True


def contains_siblings(pass_cand):
    groups = set(str(pass_cand))
    return any(str(pass_cand).count(ch) == 2 for ch in groups)


if __name__ == "__main__":
    password_range = [183564, 657474]
    print(main(password_range))
