def main():
    lines = read_input('input/8_1.txt')
    width = len(lines[0])
    height = len(lines)

    nodes = dict()
    antinodes = set()
    for line_num, line in enumerate(lines):
        for line_pos, node in enumerate(line):
            if node == '.':
                continue
            if node not in nodes:
                nodes[node] = list()
            nodes[node].append((line_num, line_pos))

    for node, positions in nodes.items():
        for pos_idx, position in enumerate(positions):
            if pos_idx == len(positions):
                continue
            for next_position in positions[pos_idx + 1:]:
                diff = ((next_position[0] - position[0]), (next_position[1] - position[1]))
                antinode_a = (position[0] - diff[0], position[1] - diff[1])
                antinode_b = (next_position[0] + diff[0], next_position[1] + diff[1])
                if 0 <= antinode_a[0] < height and 0 <= antinode_a[1] < width:
                    antinodes.add(antinode_a)
                if 0 <= antinode_b[0] < height and 0 <= antinode_b[1] < width:
                    antinodes.add(antinode_b)

    print(len(antinodes))


def read_input(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    return lines


if __name__ == "__main__":
    main()
