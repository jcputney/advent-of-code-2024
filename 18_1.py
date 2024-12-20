import heapq
import time
from enum import Enum


# switch to using tuples for directions because heapq doesn't like complex numbers
class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)


class Maze:
    def __init__(self, coordinates: []):
        self.size = 71
        self.start_pos = (1, 1)
        self.goal = (self.size, self.size)
        self.byte_count = 1025

        self.current_direction = Direction.EAST

        self.grid = {}

        # Add walls around the grid
        for x in range(self.size + 2):
            for y in range(self.size + 2):
                if y == 0 or y == self.size + 1 or x == 0 or x == self.size + 1:
                    self.grid[(x, y)] = "#"

        for i in range(min(len(coordinates), self.byte_count)):
            x, y = coordinates[i]
            self.grid[(x + 1, y + 1)] = "#"

    def find_cheapest_paths_to_goal(self):
        queue = []
        count = 0
        # keep a running count of the number of paths we've explored to break ties
        heapq.heappush(queue, (0, count, (self.start_pos,), self.start_pos, self.current_direction))

        min_steps = float('inf')
        minimal_paths = set()
        visited = {}

        while queue:
            steps, _, path, current, current_direction = heapq.heappop(queue)

            # If we've found a cheaper route to get here with the same direction, skip
            if (current, current_direction) in visited and visited[
                (current, current_direction)] < steps:
                continue
            visited[(current, current_direction)] = steps

            # If current steps is already worse than a known minimal steps, skip
            if steps > min_steps:
                continue

            # Check if we've reached the goal
            if current == self.goal:
                if steps < min_steps:
                    min_steps = steps
                    minimal_paths = {path}
                elif steps == min_steps:
                    minimal_paths.add(path)
                continue

            # Explore neighbors, prioritize current direction
            directions = [current_direction] + [d for d in Direction if d != current_direction]

            for direction in directions:
                # don't move backwards
                if steps > 0 and direction.value == (
                -current_direction.value[0], -current_direction.value[1]):
                    continue

                dx, dy = direction.value
                new_position = (current[0] + dx, current[1] + dy)
                if self.grid.get(new_position) == "#":
                    continue

                new_steps = steps + 1

                # Prune if steps exceeds current known minimal steps
                if new_steps > min_steps:
                    continue

                new_path = path + (new_position,)
                count += 1

                # prioritize current direction, keep going straight
                priority = new_steps if direction == current_direction else new_steps + 1
                heapq.heappush(queue, (priority, count, new_path, new_position, direction))

        return minimal_paths


def main():
    before = time.perf_counter()

    with open('input/18_1.txt') as f:
        coord_lines = f.read().splitlines()

    coordinates = [tuple(map(int, line.split(","))) for line in coord_lines]

    maze = Maze(coordinates)
    all_minimal_paths = maze.find_cheapest_paths_to_goal()

    shortest_path = all_minimal_paths.pop()
    print("Minimum number of steps:", len(shortest_path) - 1)

    print(f"Time taken: {time.perf_counter() - before:.2f}s")


if __name__ == "__main__":
    main()
