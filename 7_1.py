def main():
    lines = read_input('input/7_1.txt')
    result = 0
    for line in lines:
        result += check_equation(line)

    print(result)



def check_equation(line: str) -> int:
    sides = line.split(': ')
    total = int(sides[0])
    numbers = list(map(int, sides[1].split(' ')))
    operator_count = (len(numbers) - 1)

    for i in range(2 ** operator_count):
        permutation_binary = f'{i:0{operator_count}b}'
        current_total = numbers[0]
        for idx, digit in enumerate(permutation_binary):
            if digit == '1':
                current_total += numbers[idx + 1]
            else:
                current_total *= numbers[idx + 1]
        if current_total == total:
            return total

    return 0


def read_input(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines


if __name__ == "__main__":
    main()
