moves = ["^", ">", "v", "<"]
rules = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    with open("input/6_1.txt") as f:
        lines = f.read().splitlines()

        obstacles = []
        current_pos = ()
        current_dir = ""
        for line_idx, line in enumerate(lines):
            for pos_idx, pos in enumerate(line):
                if pos in moves:
                    current_dir = moves.index(pos)
                    current_pos = (line_idx, pos_idx)
                elif pos == "#":
                    obstacles.append((line_idx, pos_idx))

        print("Obstacles: ", obstacles)
        print("Start Position: ", current_pos)

        already_visited = {current_pos}
        while True:
            if current_pos[0] == 0 or current_pos[0] == len(lines) - 1 or current_pos[1] == 0 or current_pos[1] == len(lines[0]) - 1:
                break

            rule = rules[current_dir]

            new_pos = (current_pos[0] + rule[0], current_pos[1] + rule[1])
            if new_pos in obstacles:
                current_dir = (current_dir + 1) % 4
                print("New Direction: ", moves[current_dir])
                continue

            current_pos = new_pos
            if current_pos not in already_visited:
                already_visited.add(current_pos)

            print("New Position: ", current_pos)

        print("Move Count: ", len(already_visited))


if __name__ == "__main__":
    main()
