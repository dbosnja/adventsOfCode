#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/4#part1

REQUIRED_FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
OPTIONAL_FIELDS = ("cid",)


def get_valid_passports(file_path):
    """return the number of valid passports stored in input file
    
    :param file_path: str
    :rtype: int
    """
    a_passport = []
    valid_passports_number = 0
    with open(file_path) as f:
        for line in f:
            if not line.strip():
                # end of one passport(except last one!)
                if is_valid_passport(a_passport):
                    valid_passports_number += 1
                a_passport = []
            else:
                a_passport.extend(get_keys(line.strip()))
    # don't forget about the last passport
    if is_valid_passport(a_passport): valid_passports_number += 1
    return valid_passports_number


def is_valid_passport(passport):
    """return True if passport is valid

    :param passport: a list with key, value pairs
    :rtype: bool
    """
    if not all(req_key in passport for req_key in REQUIRED_FIELDS): return False
    return True


def get_keys(line):
    """return keys from key:value pairs stored in line

    :param line: represent one line in input
    :rtype: list
    """
    return [item.split(":")[0] for item in line.split(" ")]


def main():
    file_path = "input.txt"
    return get_valid_passports(file_path)


if __name__ == "__main__":
    number_of_valid_passports = main()
    print(f"{number_of_valid_passports}")
