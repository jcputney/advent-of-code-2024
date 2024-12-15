import re


def main():
    width = 101
    height = 103

    max_seconds = width * height

    with open('input/14_2.txt') as f:
        lines = f.read().splitlines()

    robots = get_robots(lines)

    lowest_safety = (0, float('inf'))

    for seconds in range(1, max_seconds):
        safety_factor = simulate_seconds(width, height, robots, seconds)
        if safety_factor < lowest_safety[1]:
            lowest_safety = (seconds, safety_factor)
    print(lowest_safety) # this was my initial guess, which actually ended up being correct


def simulate_seconds(width, height, robots, seconds):
    mid_x, mid_y = width // 2, height // 2

    final_positions = []
    for x, y, vx, vy in robots:
        nx, ny = (x + seconds * vx) % width, (y + seconds * vy) % height
        final_positions.append((nx, ny))

    quadrant_counts = [0, 0, 0, 0]
    for x, y in final_positions:
        if x < mid_x and y < mid_y:
            quadrant_counts[0] += 1
        elif x > mid_x and y < mid_y:
            quadrant_counts[1] += 1
        elif x < mid_x and y > mid_y:
            quadrant_counts[2] += 1
        elif x > mid_x and y > mid_y:
            quadrant_counts[3] += 1

    if seconds % height == 22 or seconds % height == 77: # these were the seconds where I started to see a pattern
        grid = [['.' for _ in range(width)] for _ in range(height)]
        for x, y in final_positions:
            grid[y][x] = '#'
        for row in grid:
            print(''.join(row))
        print()
        print(seconds)

    return quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]


def get_robots(lines: list) -> list:
    robots = []
    robot_regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        x, y, dx, dy = map(int, re.match(robot_regex, line).groups())
        robots.append((x, y, dx, dy))
    return robots


if __name__ == "__main__":
    main()
