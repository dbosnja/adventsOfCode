#! /usr/bin/python3.9
# https://adventofcode.com/2019/day/5 - part 2


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
    elif op_code in (3, 4):
        op_code_map["first"] = instruction_set[pointer + 1]
        op_code_map["ptr_increment"] = 2
    elif op_code in (5, 6):
        op_code_map["first"] = instruction_set[pointer + 1]
        op_code_map["second"] = instruction_set[pointer + 2]
        op_code_map["ptr_increment"] = 3
    else:
        raise ValueError("Wtf?")
    return op_code_map


def resolve_ternaries(op_map, params, instruction_set, addition=True):
    if params[-1] == "0":
        first = instruction_set[op_map["first"]]
    else:
        first = op_map["first"]
    if params[-2] == "0":
        second = instruction_set[op_map["second"]]
    else:
        second = op_map["second"]
    if addition:
        return first + second
    else:
        return first * second


def resolve_jumps(op_map, params, instruction_set, jump_true=True):
    if params[-1] == "0":
        value1 = instruction_set[op_map["first"]]
    else:
        value1 = op_map["first"]
    if params[-2] == "0":
        value2 = instruction_set[op_map["second"]]
    else:
        value2 = op_map["second"]
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


def resolve_relations(op_map, params, instruction_set, less_than=True):
    if params[-1] == "0":
        first = instruction_set[op_map["first"]]
    else:
        first = op_map["first"]
    if params[-2] == "0":
        second = instruction_set[op_map["second"]]
    else:
        second = op_map["second"]
    if less_than:
        return 1 if first < second else 0
    else:
        return 1 if first == second else 0


def main():
    file_path = "input.txt"
    instruction_set = get_input(file_path)
    input_value = 5
    pointer_instruction = 0
    while True:
        op_map = get_opcode(instruction_set, pointer_instruction)
        if op_map == False:
            break
        op_code = op_map["op_code"]
        params = op_map["params"]
        if op_code == 1:
            res = resolve_ternaries(op_map, params, instruction_set)
            instruction_set[op_map["third"]] = res
        elif op_code == 2:
            res = resolve_ternaries(op_map, params, instruction_set, False)
            instruction_set[op_map["third"]] = res
        elif op_code == 3:
            instruction_set[op_map["first"]] = input_value
        elif op_code == 4:
            print(instruction_set[op_map["first"]])
        elif op_code == 5:
            cond, ptr = resolve_jumps(op_map, params, instruction_set)
            if cond:
                pointer_instruction = ptr
            else:
                pointer_instruction += ptr
        elif op_code == 6:
            cond, ptr = resolve_jumps(op_map, params, instruction_set, False)
            if cond:
                pointer_instruction = ptr
            else:
                pointer_instruction += ptr
        elif op_code == 7:
            value = resolve_relations(op_map, params, instruction_set)
            instruction_set[op_map["third"]] = value
        elif op_code == 8:
            value = resolve_relations(op_map, params, instruction_set, False)
            instruction_set[op_map["third"]] = value

        if op_code not in (5, 6):
            pointer_instruction += op_map["ptr_increment"]


if __name__ == "__main__":
    main()
