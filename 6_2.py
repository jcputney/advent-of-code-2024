import multiprocessing as mp

moves = ["^", ">", "v", "<"]
rules = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    lines, obstacles, starting_dir, starting_pos = read_input('input/6_2.txt')

    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.starmap(check_position, [
            (lines, obstacles, starting_dir, starting_pos, line_idx, pos_idx)
            for line_idx, line in enumerate(lines)
            for pos_idx, pos in enumerate(line)
            if (line_idx, pos_idx) not in obstacles and (line_idx, pos_idx) != starting_pos
        ])

    loop_count = sum(results)
    print("Loop Count:", loop_count)


def check_position(lines, obstacles, starting_dir, starting_pos, line_idx, pos_idx):
    current_pos = starting_pos
    current_dir = starting_dir
    already_visited = {(current_pos[0], current_pos[1], current_dir)}
    new_obstacle = (line_idx, pos_idx)

    while True:
        if is_at_border(current_pos, lines):
            return False

        rule = rules[current_dir]
        new_pos = (current_pos[0] + rule[0], current_pos[1] + rule[1])

        if new_pos in obstacles or new_pos == new_obstacle:
            current_dir = (current_dir + 1) % 4
        else:
            current_pos = new_pos

        current_pos_dir = (current_pos[0], current_pos[1], current_dir)
        if current_pos_dir in already_visited:
            return True
        already_visited.add(current_pos_dir)


def is_at_border(pos, lines):
    return pos[0] == 0 or pos[0] == len(lines) - 1 or pos[1] == 0 or pos[1] == len(lines[0]) - 1


def read_input(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    obstacles = set()
    starting_pos = ()
    starting_dir = -1
    for line_idx, line in enumerate(lines):
        for pos_idx, pos in enumerate(line):
            if pos in moves:
                starting_dir = moves.index(pos)
                starting_pos = (line_idx, pos_idx)
            elif pos == "#":
                obstacles.add((line_idx, pos_idx))

    return lines, obstacles, starting_dir, starting_pos


if __name__ == "__main__":
    main()
