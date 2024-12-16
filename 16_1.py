from enum import Enum


class Direction(Enum):
    NORTH = -1j
    SOUTH = 1j
    WEST = -1
    EAST = 1


class Maze:
    def __init__(self, grid_lines: list[str]):
        self.reindeer = None
        self.goal = None

        self.move_cost = 1
        self.turn_cost = 1000

        self.current_direction = Direction.EAST

        self.grid = {}
        for y, row in enumerate(grid_lines):
            for x, cell in enumerate(row):
                location = x + y * 1j
                self.grid[location] = cell
                if cell == "S":
                    self.reindeer = location
                elif cell == "E":
                    self.goal = location

    def find_cheapest_path_to_goal(self):
        visited = set()
        queue = [(0, self.reindeer, self.current_direction)]
        min_cost = float('inf')

        while queue:
            cost, current, current_direction = min(queue, key=lambda x: x[0])
            queue.remove((cost, current, current_direction))

            if current in visited:
                continue
            visited.add(current)

            if current == self.goal:
                min_cost = min(min_cost, cost)
                continue

            for direction in Direction:
                new_cost = cost + self.move_cost
                if direction != current_direction:
                    new_cost += self.turn_cost
                new_position = current + direction.value

                if self.grid.get(new_position) == "#":
                    continue

                queue.append((new_cost, new_position, direction))

        return min_cost


def main():
    with open('input/16_1.txt') as f:
        grid_lines = f.read().splitlines()

    maze = Maze(grid_lines)
    print("Total:", maze.find_cheapest_path_to_goal())


if __name__ == "__main__":
    main()
