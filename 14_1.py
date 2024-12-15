import re

def main():
    seconds = 100

    width = 101
    height = 103
    mid_x, mid_y = width // 2, height // 2

    with open('input/14_1.txt') as f:
        lines = f.read().splitlines()

    robots = get_robots(lines)

    final_positions = []
    for x, y, vx, vy in robots:
        nx, ny = (x + seconds * vx) % width, (y + seconds * vy) % height
        if nx != mid_x and ny != mid_y:
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

    safety_factor = quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]
    print(safety_factor)


def get_robots(lines: list) -> list:
    robots = []
    robot_regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    for line in lines:
        x, y, dx, dy = map(int, re.match(robot_regex, line).groups())
        robots.append((x, y, dx, dy))
    return robots

if __name__ == "__main__":
    main()
