import multiprocessing as mp
from itertools import product

def main():
    lines = read_input('input/7_2.txt')
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.map(check_equation, lines)
    print(sum(results))



def check_equation(line: str) -> int:
    sides = line.split(': ')
    total = int(sides[0])
    numbers = list(map(int, sides[1].split(' ')))
    operator_count = (len(numbers) - 1)

    for operators in product(['+', '*', '||'], repeat=operator_count):
        current_total = numbers[0]
        for idx, operator in enumerate(operators):
            if operator == '+':
                current_total += numbers[idx + 1]
            elif operator == '*':
                current_total *= numbers[idx + 1]
            else:
                current_total = int(str(current_total) + str(numbers[idx + 1]))
        if current_total == total:
            return total

    return 0


def read_input(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines


if __name__ == "__main__":
    main()
