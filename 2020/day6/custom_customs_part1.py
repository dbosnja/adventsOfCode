#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/6 - part one


def get_all_group_answers(file_path):
    """read the input file and return the sum of answers by each group
    
    :param file_path: str
    :rtype: int
    """
    group_answers = set()
    number_of_answers_overall = 0
    with open(file_path) as f:
        # return get_number_of_answers(f.readlines())
        for line in f:
            if not line.strip():
                # end of one group
                number_of_answers_overall += len(group_answers)
                group_answers = set()
            else:
                for answer in line.strip():
                    group_answers.add(answer)
    # don't forget the last group
    number_of_answers_overall += len(group_answers)
    return number_of_answers_overall


def main():
    file_path = "input.txt"
    print(f"{get_all_group_answers(file_path)}")


if __name__ == "__main__":
    main()
    