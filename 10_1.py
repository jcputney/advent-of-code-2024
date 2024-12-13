def main():
    with open('input/10_1.txt') as f:
        lines = f.read().splitlines()

    # convert lines to a matrix of integers
    lines = [[int(char) for char in line] for line in lines]

    total = 0
    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            if char == 0:
                total += walk_path((line_idx, char_idx), 0, lines)

    print(total)


def walk_path(current_position: tuple[int, int], current_value: int, lines: list[list[int]], found=None) -> int:
    if found is None:
        found = set()

    if current_value == 9 and current_position not in found:
        found.add(current_position)
        return 1

    score = 0
    width = len(lines[0])
    height = len(lines)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dy, dx in directions:
        new_y, new_x = current_position[0] + dy, current_position[1] + dx
        if 0 <= new_y < height and 0 <= new_x < width and lines[new_y][new_x] == current_value + 1:
            score += walk_path((new_y, new_x), current_value + 1, lines, found)

    return score


if __name__ == "__main__":
    main()