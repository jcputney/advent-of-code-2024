import time
from enum import Enum


class Direction(Enum):
    NORTH = -1j
    SOUTH = 1j
    WEST = -1
    EAST = 1


def get_diamond_area(position, radius):
    points = set()
    for dx in range(-radius, radius + 1):
        dy = radius - abs(dx)
        points.add(position + dx + dy * 1j)
        points.add(position + dx - dy * 1j)
    return points


class Maze:
    def __init__(self, grid_lines: list[str]):
        self.start = None
        self.goal = None
        self.savings_goal = 100

        self.path = []
        self.path_indices = {}
        self.grid = {}
        self.height = len(grid_lines)
        self.width = len(grid_lines[0])
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
            self.path_indices[current] = len(self.path) - 1

            if current == self.goal:
                break

            for direction in Direction:
                new_position = current + direction.value
                if self.grid.get(new_position) != "#" and new_position not in visited:
                    current = new_position
                    break

    def calculate_cheat_savings(self, position):
        savings = []
        max_steps = 20

        for steps in range(1, max_steps + 1):
            diamond_points = get_diamond_area(position, steps)

            for point in diamond_points:
                if self.grid.get(point) != "#" and point in self.path_indices:
                    savings.append((point, steps))

        return savings

    def evaluate_cheats(self):
        all_savings = []
        for position in self.path:
            savings = self.calculate_cheat_savings(position)
            for end, steps in savings:
                skipped = self.path_indices[end] - self.path_indices[position] - steps
                if skipped >= self.savings_goal:
                    all_savings.append((position, end, skipped))
        return all_savings


def main():
    before = time.perf_counter()
    with open('input/20_2.txt') as f:
        grid_lines = f.read().splitlines()

    maze = Maze(grid_lines)
    maze.build_path_to_goal()

    all_savings = maze.evaluate_cheats()

    print("Number of cheats:", len(all_savings))
    print(f"Time: {time.perf_counter() - before:.4f}s")


if __name__ == "__main__":
    main()
