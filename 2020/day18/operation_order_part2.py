#! /usr/bin/python3.9
# https://adventofcode.com/2020/day/18#part2

from functools import reduce


def get_tasks(file_path):
    """read the input file

    :param file_path: file path to input file --> str
    :rtype: list
    """
    tasks = []
    with open(file_path) as f:
        for line in f:
            tasks.append(line.strip())
    return tasks


def operate_on(a, b, operand):
    """
    :param a: first operand --> int
    :param b: second operand --> int
    :param operand: '+' or '*'
    :rtype: int
    """
    a, b = tuple(map(int, (a, b)))
    if operand == '+':
        return a + b
    return a * b


def solve_task(task, i=-1):
    """solve the task and return the result

       a) operators included: +, *
       b) operands included: signed integers
       c) operators order is defined by the workflow section

       Basic workflow: the highest precedence is as always '(' and ')'
       afterwads is '+' operator and the least importan operator is '*'
       Existence of the parentheses changes the work flow to enter
       recursion state where every '(' opens a new recursion depth
       an ')' close it analogously. However, the principle of the
       actual operations remains same.

    :param task: string expression representing one task
    :param i: poistion of the element in the task --> int
    :rtype: int
    """
    # simulate the data stacks
    operators_stack, operands_stack = [], []
    # all products to be calculated
    products_stack = []
    while True:
        i += 1
        if i == len(task):
            # we hit the end of the task
            break
        char = task[i]
        if not char.strip(): continue
        if char == ")":
            return (i, reduce(int.__mul__, products_stack))
        elif char == "(":
            i, block_solution = solve_task(task, i)
            resolve_block_output(block_solution, operators_stack,
                                 operands_stack, products_stack)
        elif char.isdigit():
            resolve_block_output(char, operators_stack,
                                operands_stack, products_stack)
        elif char == "*":
            pass
        elif char == "+":
            operators_stack.append(char)
            products_stack.pop()
    return reduce(int.__mul__, products_stack)


def resolve_block_output(block_solution, operators_stack,
                         operands_stack, products_stack):
    """perform operation with a block_solution if there's an operator available.
       otherwise save the operand for the next encountered digit

    :param block_solution: int
    :param operators_stack: list
    :param operands_stack: list
    :param products_stack: list
    :rtype: NoneType
    """
    if operators_stack:
        operator = operators_stack.pop()
        if operands_stack:
            a = operands_stack.pop()
            operands_stack.append(operate_on(a, block_solution, operator))
            # add it as a potential future product
            products_stack.append(operate_on(a, block_solution, operator))
        else:
            # edge case when there are one operator and the right operand
            # also, it only makes sense for operator to be '+'
            operands_stack.append(operate_on(0, block_solution, operator))
            # add it as a potential future product
            products_stack.append(operate_on(0, block_solution, operator))
    else:
        # no operators so far, just add the operand
        operands_stack.append(int(block_solution))
        # add it as a potential future product
        products_stack.append(int(block_solution))


def main():
    file_path = "input.txt"
    tasks = get_tasks(file_path)
    # data loaded
    solutions = []
    for task in tasks:
        solutions.append(solve_task(task))
    return sum(solutions)


if __name__ == "__main__":
    print(main())
