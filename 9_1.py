def main():
    with open('input/9_1.txt') as f:
        contents = ''.join(f.read().splitlines())

    layout = []
    for idx, char in enumerate(contents):
        for _ in range(int(char)):
            layout.append(str(idx // 2 if idx % 2 == 0 else '.'))

    layout = compress_disk(layout)

    total = sum(int(char) * idx for idx, char in enumerate(layout[:layout.index('.')]))

    print(total)


def compress_disk(layout: list[str]) -> list[str]:
    first_space = 0
    last_block = len(layout) - 1
    while first_space < last_block:
        while layout[first_space] != '.':
            first_space += 1
        while layout[last_block] == '.':
            last_block -= 1
        if first_space < last_block:
            layout[first_space], layout[last_block] = layout[last_block], layout[first_space]
            first_space += 1
            last_block -= 1
    return layout


if __name__ == "__main__":
    main()
