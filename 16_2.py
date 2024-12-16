from enum import Enum
import heapq

# switch to using tuples for directions because heapq doesn't like complex numbers
class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)

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
                location = (x, y)
                self.grid[location] = cell
                if cell == "S":
                    self.reindeer = location
                elif cell == "E":
                    self.goal = location

    def find_cheapest_paths_to_goal(self):
        queue = []
        count = 0
        # keep a running count of the number of paths we've explored to break ties
        heapq.heappush(queue, (0, count, (self.reindeer,), self.reindeer, self.current_direction))

        min_cost = float('inf')
        minimal_paths = set()
        visited = {}

        while queue:
            cost, _, path, current, current_direction = heapq.heappop(queue)

            # If we've found a cheaper route to get here with the same direction, skip
            if (current, current_direction) in visited and visited[(current, current_direction)] < cost:
                continue
            visited[(current, current_direction)] = cost

            # If current cost is already worse than a known minimal cost, skip
            if cost > min_cost:
                continue

            # Check if we've reached the goal
            if current == self.goal:
                if cost < min_cost:
                    min_cost = cost
                    minimal_paths = {path}
                elif cost == min_cost:
                    minimal_paths.add(path)
                continue

            # Explore neighbors
            for direction in Direction:
                dx, dy = direction.value
                new_position = (current[0] + dx, current[1] + dy)
                if self.grid.get(new_position) == "#":
                    continue

                new_cost = cost + self.move_cost
                if direction != current_direction:
                    new_cost += self.turn_cost

                # Prune if cost exceeds current known minimal cost
                if new_cost > min_cost:
                    continue

                new_path = path + (new_position,)
                count += 1
                heapq.heappush(queue, (new_cost, count, new_path, new_position, direction))

        return minimal_paths

def main():
    with open('input/16_2.txt') as f:
        grid_lines = f.read().splitlines()

    maze = Maze(grid_lines)
    all_minimal_paths = maze.find_cheapest_paths_to_goal()

    print("Number of minimal cost paths:", len(all_minimal_paths))
    total_unique_positions = len(set(pos for p in all_minimal_paths for pos in p))
    print("Total unique positions in all minimal paths:", total_unique_positions)

if __name__ == "__main__":
    main()
