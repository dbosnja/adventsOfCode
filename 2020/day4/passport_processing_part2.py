#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/4#part2
import re


def check_height_field(value):
    """check if value is in valid form ie
       first check the measure unit, cm or in
       and then the range

    :param value: str
    :rtype: bool
    """
    pattern_match = re.match(r'^\d+(cm|in)$', value)
    if not pattern_match: return False
    if pattern_match.group(1) == "cm":
        return int(value.replace("cm", "")) in range(150, 194)
    return int(value.replace("in", "")) in range(59, 77)


def get_valid_passports(file_path):
    """return the number of valid passports stored in input file
    
    :param file_path: str
    :rtype: int
    """
    a_passport = {}
    valid_passports_number = 0
    with open(file_path) as f:
        for line in f:
            if not line.strip():
                # end of one passport(except last one!)
                if is_valid_passport(a_passport):
                    valid_passports_number += 1
                a_passport = {}
            else:
                a_passport.update(get_key_value(line.strip()))
    # don't forget about the last passport
    if is_valid_passport(a_passport): valid_passports_number += 1
    return valid_passports_number


def is_valid_passport(passport):
    """return True if passport is valid

    :param passport: dict
    :rtype: bool
    """
    valid_field_map_src = """valid_field_map = \
{"byr": int(passport.get("byr", 0)) in range(1920, 2003), 
"iyr": int(passport.get("iyr", 0)) in range(2010, 2021), 
"eyr": int(passport.get("eyr", 0)) in range(2020, 2031),
"hgt": check_height_field(passport.get("hgt", "")), 
"hcl": re.match(r'^#[a-f, 0-9]{6}$', passport.get("hcl", '#')),
"ecl": passport.get("ecl", "") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",], 
"pid": re.match(r'^\d{9}$', passport.get("pid", ""))}
"""
    
    exec(valid_field_map_src)
    # check quantity
    if not all(req_key in passport for req_key in locals()['valid_field_map']): return False
    # check quality
    if not all(locals()['valid_field_map'].values()): return False
    return True


def get_key_value(line):
    """return key,value from key:value pairs stored in line

    :param line: represent one line in input
    :rtype: [(key, value)]
    """
    return [item.split(":") for item in line.split(" ")]


def main():
    file_path = "input.txt"
    return get_valid_passports(file_path)


if __name__ == "__main__":
    number_of_valid_passports = main()
    print(f"{number_of_valid_passports}")
