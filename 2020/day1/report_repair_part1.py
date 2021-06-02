#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/1 - part one


def get_expense_report(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]


def get_adders(expense_report):
    """" return first combination of two elements in expense_report
         which sum up to 2020

    :param expense_report: list of int
    :rtype: tuple
    """
    requested_sum = 2020
    for adder1 in expense_report:
        for adder2 in expense_report:
            if adder1 + adder2 == requested_sum: return adder1, adder2



def main():
    file_path = "input.txt"
    expense_report_list = get_expense_report(file_path)
    adder1, adder2 = get_adders(expense_report_list)
    return adder1 * adder2


if __name__ == "__main__":
    resulting_product = main()
    print(f"{resulting_product}")