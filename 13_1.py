import re


def main():
    with open('input/13_1.txt') as f:
        lines = f.read().splitlines()

    idx = 0
    machines = []

    button_a_cost = 3
    button_b_cost = 1

    button_a_regex = r"Button A: X([-+]\d+), Y([-+]\d+)"
    button_b_regex = r"Button B: X([-+]\d+), Y([-+]\d+)"
    prize_regex = r"Prize: X=(\d+), Y=(\d+)"

    while idx < len(lines):
        button_a = tuple(map(int, re.match(button_a_regex, lines[idx]).groups()))
        button_b = tuple(map(int, re.match(button_b_regex, lines[idx + 1]).groups()))
        prize = tuple(map(int, re.match(prize_regex, lines[idx + 2]).groups()))
        machines.append((button_a, button_b, prize))
        idx += 4

    print(machines)

    total = 0
    # brute force a solution
    for machine in machines:
        button_a, button_b, prize = machine
        x, y = prize

        b_pushes = max(min(x // button_b[0], y // button_b[1]), 100)

        a_pushes = 0
        while b_pushes >= 0:
            if (b_pushes * button_b[0] + a_pushes * button_a[0]) == x and (
                    b_pushes * button_b[1] + a_pushes * button_a[1]) == y:
                total += a_pushes * button_a_cost + b_pushes * button_b_cost
                break
            a_pushes += 1
            if a_pushes > 100 or (b_pushes * button_b[0] + a_pushes * button_a[0]) > x or \
                    (b_pushes * button_b[1] + a_pushes * button_a[1]) > y:
                a_pushes = 0
                b_pushes -= 1

    print("Total:", total)


if __name__ == "__main__":
    main()
