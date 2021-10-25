#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/9 - part 1


def get_input(file_path):
    with open(file_path) as f:
        return [int(i) for i in f.read().strip().split(",")]


def get_opcode(instruction_set, pointer):
    instr_code = str(instruction_set[pointer])
    op_code = instr_code[-2:]
    parameters = instr_code.replace(op_code, "").zfill(3)
    op_code = int(op_code)
    op_code_map = {
        "op_code": op_code,
        "params": parameters,
    }
    if op_code == 99:
        # terminate whole test
        return False
    elif op_code in (1, 2, 7, 8):
        op_code_map["first"] = instruction_set[pointer + 1]
        op_code_map["second"] = instruction_set[pointer + 2]
        op_code_map["third"] = instruction_set[pointer + 3]
        op_code_map["ptr_increment"] = 4
    elif op_code in (3, 4, 9):
        op_code_map["first"] = instruction_set[pointer + 1]
        op_code_map["ptr_increment"] = 2
    elif op_code in (5, 6):
        op_code_map["first"] = instruction_set[pointer + 1]
        op_code_map["second"] = instruction_set[pointer + 2]
        op_code_map["ptr_increment"] = 3
    else:
        raise ValueError("Wtf?")
    return op_code_map


def resolve_ternaries(op_map, params, instruction_set, relative_base, addition=True):
    if params[-1] == "0":
        first = instruction_set[op_map["first"]]
    elif params[-1] == "1":
        first = op_map["first"]
    else:
        first = instruction_set[op_map["first"] + relative_base]

    if params[-2] == "0":
        second = instruction_set[op_map["second"]]
    elif params[-2] == "1":
        second = op_map["second"]
    else:
        second = instruction_set[op_map["second"] + relative_base]

    if params[-3] == "0":
        third = op_map["third"]
    else:
        third = op_map["third"] + relative_base

    if addition:
        return first + second, third
    else:
        return first * second, third


def resolve_jumps(op_map, params, instruction_set, relative_base, jump_true=True):
    if params[-1] == "0":
        value1 = instruction_set[op_map["first"]]
    elif params[-1] == "1":
        value1 = op_map["first"]
    else:
        value1 = instruction_set[op_map["first"] + relative_base]

    if params[-2] == "0":
        value2 = instruction_set[op_map["second"]]
    elif params[-2] == "1":
        value2 = op_map["second"]
    else:
        value2 = instruction_set[op_map["second"] + relative_base]

    if jump_true:
        if value1:
            return True, value2
        else:
            return False, op_map["ptr_increment"]
    else:
        if not value1:
            return True, value2
        else:
            return False, op_map["ptr_increment"]


def resolve_relations(op_map, params, instruction_set, relative_base, less_than=True):
    if params[-1] == "0":
        first = instruction_set[op_map["first"]]
    elif params[-1] == "1":
        first = op_map["first"]
    else:
        first = instruction_set[op_map["first"] + relative_base]

    if params[-2] == "0":
        second = instruction_set[op_map["second"]]
    elif params[-2] == "1":
        second = op_map["second"]
    else:
        second = instruction_set[op_map["second"] + relative_base]

    if params[-3] == "0":
        third = op_map["third"]
    else:
        third = op_map["third"] + relative_base

    if less_than:
        return 1 if first < second else 0, third
    else:
        return 1 if first == second else 0, third


def adjust_relative_base(op_map, params, instruction_set, relative_base):
    value = op_map["first"]
    mode = params[-1]
    if mode == '0':
        return instruction_set[value]
    elif mode == '1':
        return value
    else:
        return instruction_set[value + relative_base]


def main():
    file_path = "input.txt"
    instruction_set = get_input(file_path)
    instruction_set += [0 for i in range(100)]
    input_value = 1
    pointer_instruction = 0
    relative_base = 0
    while True:
        op_map = get_opcode(instruction_set, pointer_instruction)
        if op_map == False:
            break
        op_code = op_map["op_code"]
        params = op_map["params"]
        if op_code == 1:
            res, address = resolve_ternaries(op_map, params, instruction_set, relative_base)
            instruction_set[address] = res
        elif op_code == 2:
            res, address = resolve_ternaries(op_map, params, instruction_set, relative_base, False)
            instruction_set[address] = res
        elif op_code == 3:
            if params[-1] == "0":
                instruction_set[op_map["first"]] = input_value
            else:
                instruction_set[op_map["first"] + relative_base] = input_value
        elif op_code == 4:
            if params[-1] == "0":
                print(instruction_set[op_map["first"]])
            elif params[-1] == "1":
                print(op_map["first"])
            else:
                print(instruction_set[op_map["first"] + relative_base])
        elif op_code == 5:
            cond, ptr = resolve_jumps(op_map, params, instruction_set, relative_base)
            if cond:
                pointer_instruction = ptr
            else:
                pointer_instruction += ptr
        elif op_code == 6:
            cond, ptr = resolve_jumps(op_map, params, instruction_set, relative_base, False)
            if cond:
                pointer_instruction = ptr
            else:
                pointer_instruction += ptr
        elif op_code == 7:
            value, address = resolve_relations(op_map, params, instruction_set, relative_base)
            instruction_set[address] = value
        elif op_code == 8:
            value, address = resolve_relations(op_map, params, instruction_set, relative_base, False)
            instruction_set[address] = value
        elif op_code == 9:
            relative_base += adjust_relative_base(op_map, params, instruction_set, relative_base)
        if op_code not in (5, 6):
            pointer_instruction += op_map["ptr_increment"]



if __name__ == "__main__":
    main()
