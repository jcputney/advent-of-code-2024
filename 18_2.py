import time
from collections import deque
from enum import Enum


# switch to using tuples for directions because heapq doesn't like complex numbers
class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)


class Maze:
    def __init__(self, coordinates: list[tuple[int, int]], byte_count: int):
        self.size = 71
        self.start_pos = (1, 1)
        self.goal = (self.size, self.size)
        self.byte_count = byte_count

        self.current_direction = Direction.EAST

        self.grid = {}

        # Add walls around the grid
        for x in range(self.size + 2):
            for y in range(self.size + 2):
                if y == 0 or y == self.size + 1 or x == 0 or x == self.size + 1:
                    self.grid[(x, y)] = "#"

        for i in range(min(len(coordinates), self.byte_count)):
            x, y = coordinates[i]
            self.grid[(x + 1, y + 1)] = "#" # adjust for the walls

    def find_any_path_to_goal(self):
        queue = deque()
        queue.append((self.start_pos, self.current_direction))
        visited = set()

        while queue:
            pos, current_direction = queue.popleft()

            if pos == self.goal:
                return False  # Path exists

            if pos in visited or self.grid.get(pos) == "#":
                continue  # Skip dead ends or already visited positions

            visited.add(pos)

            # Prioritize continuing in the same direction
            directions = [current_direction] + [direction for direction in Direction if direction != current_direction]

            for direction in directions:
                new_pos = (pos[0] + direction.value[0], pos[1] + direction.value[1])
                queue.append((new_pos, direction))

        return True  # Path is blocked


def main():
    before = time.perf_counter()

    with open('input/18_2.txt') as f:
        coord_lines = f.read().splitlines()

    coordinates = [(int(x), int(y)) for x, y in (line.split(",") for line in coord_lines)]

    byte_count = 1025
    while byte_count < len(coordinates):
        maze = Maze(coordinates, byte_count)
        blocker = maze.find_any_path_to_goal()

        print("Tested byte count:", byte_count)

        if blocker:
            print(f"Byte count: {byte_count}")
            print("Blocker:", coordinates[byte_count-1])
            break

        byte_count += 1

    print(f"Time taken: {time.perf_counter() - before:.2f}s")


if __name__ == "__main__":
    main()
