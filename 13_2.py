import re
from fractions import Fraction

def main():
    with open('input/13_2.txt') as f:
        lines = f.read().splitlines()

    machines = get_machines(lines)

    button_a_cost = 3
    button_b_cost = 1
    offset = 10_000_000_000_000

    total = 0
    for (ax, ay), (bx, by), (x, y) in machines:
        x += offset
        y += offset

        # Calculate the determinant of the matrix formed by the button vectors. If the lines, never
        # intersect, skip, because we can't solve for A and B
        det = ax * by - ay * bx
        if det == 0:
            continue

        # Calculate the numerator and denominator for the fraction representing the number of B button pushes
        numerator = x * ay - y * ax
        denominator = bx * ay - by * ax
        b = Fraction(numerator, denominator)

        # If B isn't an integer, skip
        if b.denominator != 1:
            continue
        b_pushes = b.numerator

        # If ax == 0, we can't solve for A, because we'd be dividing by 0
        if ax == 0:
            continue

        a = Fraction(x - b_pushes * bx, ax)
        if a.denominator != 1:
            continue
        a_pushes = a.numerator

        if a_pushes < 0 or b_pushes < 0 or (a_pushes * ay + b_pushes * by != y):
            continue

        total += a_pushes * button_a_cost + b_pushes * button_b_cost

    print("Total cost:", total)

def get_machines(lines):
    machines = []
    button_a_regex = r"Button A: X([-+]\d+), Y([-+]\d+)"
    button_b_regex = r"Button B: X([-+]\d+), Y([-+]\d+)"
    prize_regex = r"Prize: X=(\d+), Y=(\d+)"

    idx = 0
    while idx < len(lines):
        button_a = tuple(map(int, re.match(button_a_regex, lines[idx]).groups()))
        button_b = tuple(map(int, re.match(button_b_regex, lines[idx + 1]).groups()))
        prize = tuple(map(int, re.match(prize_regex, lines[idx + 2]).groups()))
        machines.append((button_a, button_b, prize))
        idx += 4
    return machines

if __name__ == "__main__":
    main()
