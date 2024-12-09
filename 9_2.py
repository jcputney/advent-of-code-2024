def main():
    with open('input/9_2.txt') as f:
        contents = ''.join(f.read().splitlines())

    layout = parse_layout(contents)
    defragment_disk(layout)

    disk_layout = []
    for char, size in layout:
        for _ in range(size):
            disk_layout.append(char)

    total = 0
    for idx, char in enumerate(disk_layout):
        if char == '.':
            continue
        total += int(char) * idx
    print(total)


def parse_layout(contents):
    layout = []
    for idx, char in enumerate(contents):
        if idx % 2 == 0:
            layout.append((str(idx // 2), int(char)))
        else:
            layout.append(('.', int(char)))
    return layout


def defragment_disk(layout):
    rev_idx = len(layout) - 1
    while rev_idx >= 0:
        file = layout[rev_idx]
        if file[0] == '.':
            rev_idx -= 1
            continue
        for space_idx, space in enumerate(layout):
            if space[0] != '.':
                continue
            if rev_idx > space_idx and space[1] >= file[1]:
                file_idx = layout.index(file)
                layout[space_idx] = (file[0], file[1])
                if space[1] == file[1]:
                    # if the space is the same size as the file, just swap them
                    layout[file_idx] = ('.', file[1])
                    break
                else:
                    # if the space is bigger than the file, split the space and move the file
                    layout.insert(space_idx + 1, ('.', space[1] - file[1]))
                    layout[file_idx + 1] = ('.', file[1])
                    break
        rev_idx -= 1


if __name__ == "__main__":
    main()
