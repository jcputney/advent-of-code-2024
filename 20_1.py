from enum import Enum


class Direction(Enum):
    NORTH = -1j
    SOUTH = 1j
    WEST = -1
    EAST = 1


class Maze:
    def __init__(self, grid_lines: list[str]):
        self.start = None
        self.goal = None

        self.path = []

        self.grid = {}
        for y, row in enumerate(grid_lines):
            for x, cell in enumerate(row):
                location = x + y * 1j
                self.grid[location] = cell
                if cell == "S":
                    self.start = location
                elif cell == "E":
                    self.goal = location

    def build_path_to_goal(self):
        visited = set()

        current = self.start
        while True:
            visited.add(current)
            self.path.append(current)

            if current == self.goal:
                break

            for direction in Direction:
                new_position = current + direction.value

                if self.grid.get(new_position) != "#" and new_position not in visited:
                    current = new_position
                    break

    def check_cheat_savings(self, start: tuple[int, int], end: tuple[int, int]) -> int:
        if end not in self.path or start not in self.path:
            return 0
        return self.path.index(end) - self.path.index(start) - 2

    def check_all_cheats_for_position(self, position: tuple[int, int]) -> set[
        tuple[tuple[int, int], tuple[int, int]]]:
        viable_cheats = set()
        for direction in Direction:
            wall_position = position + direction.value
            end_position = wall_position + direction.value
            if self.grid.get(wall_position) == "#" and self.grid.get(end_position) != "#":
                savings = self.check_cheat_savings(position, end_position)
                if savings >= 100:
                    viable_cheats.add((position, end_position))

        return viable_cheats


def main():
    with open('input/20_1.txt') as f:
        grid_lines = f.read().splitlines()

    maze = Maze(grid_lines)
    maze.build_path_to_goal()
    all_viable_cheats = set()
    for position in maze.path:
        for cheat in maze.check_all_cheats_for_position(position):
            all_viable_cheats.add(cheat)

    print(len(all_viable_cheats))


if __name__ == "__main__":
    main()
