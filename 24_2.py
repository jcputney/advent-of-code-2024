import re
import time

XOR = 'XOR'
AND = 'AND'
OR = 'OR'

g = {}  # Dictionary: (a, b, op) -> output_wire
rg = {}  # Reverse map: output_wire -> (a, b, op)


def minmax(a, b):
    return (a, b) if a <= b else (b, a)


def swap(wire_a, wire_b):
    rg[wire_a], rg[wire_b] = rg[wire_b], rg[wire_a]

    triple_a = rg[wire_a]
    triple_b = rg[wire_b]
    g[triple_a], g[triple_b] = g[triple_b], g[triple_a]


def main():
    start_time = time.perf_counter()
    with open("input/24_2.txt", "r") as f:
        text = f.read()

    puzzle_chunks = text.split("\n\n")
    gate_lines = puzzle_chunks[1].splitlines()
    instruction_regex = r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})"
    for instruction in gate_lines:
        match = re.match(instruction_regex, instruction)
        if match:
            input1, operation, input2, output = match.groups()
            input1, input2 = minmax(input1, input2)
            g[(input1, input2, operation)] = output
            rg[output] = (input1, input2, operation)

    output = set()
    carry_wire = ''

    max_wire_name = max(rg.keys())
    max_index = int(max_wire_name[1:])

    for i in range(max_index):
        x = f"x{i:02}"
        y = f"y{i:02}"
        z = f"z{i:02}"

        # x XOR y = sum bit (without carry)
        xxy = g[(minmax(x, y) + (XOR,))]  # x ^ y
        # x AND y = carry bit from x,y
        xay = g[(minmax(x, y) + (AND,))]

        if not carry_wire:
            carry_wire = xay
        else:
            input1, input2 = minmax(carry_wire, xxy)
            k = (input1, input2, XOR)

            if k not in g:
                a2, b2, _ = rg[z]
                a, b = list({a2, b2} ^ {input1, input2})
                output.add(a)
                output.add(b)
                swap(a, b)

            elif g[k] != z:
                output.add(g[k])
                output.add(z)
                swap(z, g[k])

            xxy = g[(minmax(x, y) + (XOR,))]
            xay = g[(minmax(x, y) + (AND,))]

            carry1 = g[(minmax(carry_wire, xxy) + (AND,))]
            carry_wire = g[(minmax(carry1, xay) + (OR,))]

    print(','.join(sorted(output)))

    elapsed = time.perf_counter() - start_time
    print(f"Time elapsed: {elapsed:.4f} s")


if __name__ == "__main__":
    main()
