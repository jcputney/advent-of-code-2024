import re
import time


class ThreeBitComputer:
    def __init__(self, register_a: int, instructions: list[int]):
        self.registers = [register_a, 0, 0]
        self.instructions = instructions

        self.ins_ptr = 0
        self.output = []

    def run(self):
        while self.ins_ptr < len(self.instructions) - 1:
            opcode, operand = int(self.instructions[self.ins_ptr]), int(
                self.instructions[self.ins_ptr + 1])
            if opcode == 0:  # adv
                self.registers[0] = int(self.registers[0] / 2 ** self.combo_operand(operand))
            elif opcode == 1:  # bxl
                self.registers[1] = self.registers[1] ^ operand
            elif opcode == 2:  # bst
                self.registers[1] = self.combo_operand(operand) % 8
            elif opcode == 3:  # jnz
                if self.registers[0] == 0:
                    self.ins_ptr += 2
                    continue
                if self.ins_ptr != operand:
                    self.ins_ptr = operand - 2
            elif opcode == 4:  # bxc
                self.registers[1] = self.registers[1] ^ self.registers[2]
            elif opcode == 5:  # out
                self.output.append(self.combo_operand(operand) % 8)
            elif opcode == 6:  # bdv
                self.registers[1] = int(self.registers[0] / 2 ** self.combo_operand(operand))
            elif opcode == 7:  # cdv
                self.registers[2] = int(self.registers[0] / 2 ** self.combo_operand(operand))

            self.ins_ptr += 2

    def combo_operand(self, operand):
        if operand <= 3:
            return operand
        if operand == 4:
            return self.registers[0]
        if operand == 5:
            return self.registers[1]
        if operand == 6:
            return self.registers[2]
        print("Invalid operand:", operand)
        exit(1)


def main():
    before = time.perf_counter()

    with open('input/17_2.txt') as f:
        grid_lines = f.read().splitlines()

    program_regex = r"Program: (.*)"

    instructions = []

    for line in grid_lines:
        if match := re.match(program_regex, line):
            program = match.group(1)
            instructions = list(map(int, program.split(",")))

    # build the output backwards, starting from the end of the program
    program_length = len(instructions) - 1
    current_registers = [0]
    while program_length >= 0:
        next_registers = []
        expected_output = instructions[program_length:]
        for current_a in current_registers:
            register_a = current_a * 8
            for i in range(8): #
                computer = ThreeBitComputer(register_a + i, instructions)
                computer.run()
                if computer.output == expected_output:
                    next_registers.append(register_a + i)
        program_length -= 1
        current_registers = next_registers.copy()

    print(f"Run time: {time.perf_counter() - before:.4f}s")
    print(min(current_registers))


if __name__ == "__main__":
    main()
