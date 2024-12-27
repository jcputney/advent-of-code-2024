import re
import time


class Instruction:
    def __init__(self, input1, input2, operation, output):
        self.input1 = input1
        self.input2 = input2
        self.operation = operation
        self.output = output

    def __str__(self):
        return f"{self.input1} {self.operation} {self.input2} -> {self.output}"


class LogicCalculator:
    def __init__(self, states, instructions):
        self.states = states
        self.instructions = instructions

    def calculate(self):
        waiting = dict[(str, str), Instruction]()
        while self.instructions:
            instruction = self.instructions.pop(0)
            if instruction.input1 not in self.states or instruction.input2 not in self.states:
                waiting[(instruction.input1, instruction.input2, instruction.output)] = instruction
                continue
            if instruction.operation == "AND":
                self.states[instruction.output] = self.states[instruction.input1] & self.states[
                    instruction.input2]
            elif instruction.operation == "OR":
                self.states[instruction.output] = self.states[instruction.input1] | self.states[
                    instruction.input2]
            elif instruction.operation == "XOR":
                self.states[instruction.output] = self.states[instruction.input1] ^ self.states[
                    instruction.input2]
            pop = 0
            for key in list(waiting.keys()):
                if key[0] == instruction.output or key[1] == instruction.output:
                    waiting_instruction = waiting.pop(key)
                    self.instructions.insert(pop, waiting_instruction)
                    pop += 1

    def get_output(self):
        z_states = [state for state in self.states.keys() if state.startswith("z")]
        largest_bit = max([int(state[1:]) for state in z_states])
        bit_array = [1 if self.states[f"z{i:02}"] else 0 for i in range(largest_bit + 1)]
        return int("".join(map(str, bit_array[::-1])), 2)


def main():
    with open("input/24_1.txt", "r") as f:
        text = f.read()
        input_states = text.split("\n\n")[0].splitlines()
        input_instructions = text.split("\n\n")[1].splitlines()

    states = {}
    for state in input_states:
        key, value = state.split(": ")
        states[key] = value == "1"

    instruction_regex = r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})"
    instructions = []
    for instruction in input_instructions:
        match = re.match(instruction_regex, instruction)
        if match:
            input1, operation, input2, output = match.groups()
            instructions.append(Instruction(input1, input2, operation, output))

    start_time = time.perf_counter()

    calculator = LogicCalculator(states, instructions)
    calculator.calculate()
    output = calculator.get_output()

    print(f"Output             : {output}")

    print(f"Time elapsed       : {time.perf_counter() - start_time :.3f} s")


if __name__ == "__main__":
    main()
