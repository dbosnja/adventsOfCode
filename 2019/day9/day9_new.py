class IntCodeComputer:
    """Simulates CPU-like semantics."""
    def __init__(self, opcodes, init_value):
        self.opcodes = opcodes + [0 for _ in range(1000)]
        self.init_value = init_value
        self.ptr = 0
        self.relative_base = 0

    def addition_or_mul(self, param_modes, sign='+'):
        mode_a, mode_b, mode_c = reversed(param_modes)
        assert isinstance(mode_a, str)
        a_addr = int(self.opcodes[self.ptr + 1])
        if mode_a == '0':
            a = self.opcodes[a_addr]
        elif mode_a == '1':
            a = self.opcodes[self.ptr + 1]
        elif mode_a == '2':
            a = self.opcodes[a_addr + self.relative_base]
        else:
            raise ValueError(f'Illegal mode: {mode_a}')
        b_addr = int(self.opcodes[self.ptr + 2])
        if mode_b == '0':
            b = self.opcodes[b_addr]
        elif mode_b == '1':
            b = self.opcodes[self.ptr + 2]
        elif mode_b == '2':
            b = self.opcodes[b_addr + self.relative_base]
        else:
            raise ValueError(f'Illegal mode: {mode_a}')
        c_addr = int(self.opcodes[self.ptr + 3])
        if mode_c == '0':
            pass
        elif mode_c == '2':
            c_addr += self.relative_base
        else:
            raise ValueError(f'Illegal mode: {mode_a}')
        if sign == '+':
            self.opcodes[c_addr] = str(int(a) + int(b))
        else:
            self.opcodes[c_addr] = str(int(a) * int(b))
        self.ptr += 4

    def save_value(self, param_modes):
        mode_a = param_modes[-1]
        a_addr = int(self.opcodes[self.ptr + 1])
        if mode_a == '0':
            self.opcodes[a_addr] = str(self.init_value)
        elif mode_a == '2':
            a_addr += self.relative_base
            self.opcodes[a_addr] = str(self.init_value)
        else:
            raise ValueError(f'Illegal param: {mode_a}')
        self.ptr += 2

    def write_value(self, param_modes):
        mode_a = param_modes[-1]
        a_addr = int(self.opcodes[self.ptr + 1])
        if mode_a == '0':
            val = self.opcodes[a_addr]
        elif mode_a == '1':
            val = a_addr
        elif mode_a == '2':
            a_addr += self.relative_base
            val = self.opcodes[a_addr]
        else:
            raise ValueError(f'Illegal param: {mode_a}')
        print(val)
        self.ptr += 2

    def jump_instruction(self, param_modes, if_true=True):
        mode_a, mode_b = reversed(param_modes)
        a_addr = int(self.opcodes[self.ptr + 1])
        if mode_a == '0':
            a = self.opcodes[a_addr]
        elif mode_a == '1':
            a = a_addr
        elif mode_a == '2':
            a_addr += self.relative_base
            a = self.opcodes[a_addr]
        else:
            raise ValueError(f'Illegal param: {mode_a}')
        b_addr = int(self.opcodes[self.ptr + 2])
        if mode_b == '0':
            b = self.opcodes[b_addr]
        elif mode_b == '1':
            b = b_addr
        elif mode_b == '2':
            b_addr += self.relative_base
            b = self.opcodes[b_addr]
        else:
            raise ValueError(f'Illegal param: {mode_a}')
        if if_true:
            if int(a) != 0:
                self.ptr = int(b)
                return
        else:
            if int(a) == 0:
                self.ptr = int(b)
                return
        self.ptr += 3

    def relational_instruction(self, params_mode, less_than=True):
        mode_a, mode_b, mode_c = reversed(params_mode)
        a_addr = int(self.opcodes[self.ptr + 1])
        if mode_a == '0':
            a = self.opcodes[a_addr]
        elif mode_a == '1':
            a = a_addr
        elif mode_a == '2':
            a_addr += self.relative_base
            a = self.opcodes[a_addr]
        else:
            raise ValueError(f'Illegal param: {mode_a}')
        b_addr = int(self.opcodes[self.ptr + 2])
        if mode_b == '0':
            b = self.opcodes[b_addr]
        elif mode_b == '1':
            b = b_addr
        elif mode_b == '2':
            b_addr += self.relative_base
            b = self.opcodes[b_addr]
        else:
            raise ValueError(f'Illegal param: {mode_b}')
        c_addr = int(self.opcodes[self.ptr + 3])
        if mode_c == '0':
            pass
        elif mode_c == '2':
            c_addr += self.relative_base
        else:
            raise ValueError(f'Illegal param: {mode_c}')
        if less_than:
            self.opcodes[c_addr] = '1' if int(a) < int(b) else '0'
        else:
            self.opcodes[c_addr] = '1' if int(a) == int(b) else '0'
        self.ptr += 4

    def relative_base_instruction(self, param_modes):
        mode_a = param_modes[-1]
        a_addr = int(self.opcodes[self.ptr + 1])
        if mode_a == '0':
            val = self.opcodes[a_addr]
        elif mode_a == '1':
            val = a_addr
        elif mode_a == '2':
            a_addr += self.relative_base
            val = self.opcodes[a_addr]
        else:
            raise ValueError(f'Illegal param: {mode_a}')
        self.relative_base += int(val)
        self.ptr += 2

    def get_current_opcode(self):
        opcode = self.opcodes[self.ptr]
        param_modes, opcode = opcode[:-2], opcode[-2:]
        if not param_modes:
            param_modes = '0'
        opcode = opcode.zfill(2)
        if opcode in ('03', '04', '09'):
            param_modes = param_modes.zfill(1)
        elif opcode in ('05', '06'):
            param_modes = param_modes.zfill(2)
        elif opcode in ('01', '02', '07', '08'):
            param_modes = param_modes.zfill(3)
        elif opcode == '99':
            return None, opcode
        else:
            raise ValueError(f"Illegal opcode: {opcode}")
        return param_modes, opcode

    def run(self):
        while True:
            param_modes, op_code = self.get_current_opcode()
            if op_code == '99':
                # program executed
                return
            elif op_code == '01':
                self.addition_or_mul(param_modes)
            elif op_code == '02':
                self.addition_or_mul(param_modes, sign='*')
            elif op_code == '03':
                self.save_value(param_modes)
            elif op_code == '04':
                self.write_value(param_modes)
            elif op_code == '05':
                self.jump_instruction(param_modes)
            elif op_code == '06':
                self.jump_instruction(param_modes, if_true=False)
            elif op_code == '07':
                self.relational_instruction(param_modes)
            elif op_code == '08':
                self.relational_instruction(param_modes, less_than=False)
            elif op_code == '09':
                self.relative_base_instruction(param_modes)
            else:
                raise RuntimeError(f'Unknown Opcode: {op_code}')

    @property
    def opcode_bank(self):
        return self.opcodes


def get_input(file_path):
    with open(file_path) as f:
        return f.readline().strip().split(',')


def main():
    file_path = 'input.txt'
    opcodes = get_input(file_path)
    init_value = 2
    cpu = IntCodeComputer(opcodes, init_value)
    cpu.run()


if __name__ == '__main__':
    main()