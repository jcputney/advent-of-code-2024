def main():
    with open('input/12_1.txt') as f:
        lines = f.read().splitlines()

    visited = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]

    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if not visited[y][x]:
                dimensions = [0, 0]
                walk_region(x, y, lines[y][x], dimensions, lines, visited)
                print(
                    f"A region of `{lines[y][x]}` plants with price {dimensions[0]} * {dimensions[1]} = {dimensions[0] * dimensions[1]}")
                total += dimensions[0] * dimensions[1]

    print(total)


def walk_region(x: int, y: int, crop: str, dimensions: [int], lines: list[str],
                visited: list[list[bool]]):
    if lines[y][x] != crop or visited[y][x]:
        return

    visited[y][x] = True
    dimensions[0] += 1

    for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(lines[y]) and 0 <= ny < len(lines) and not visited[ny][nx]:
            walk_region(nx, ny, crop, dimensions, lines, visited)
        if nx < 0 or nx >= len(lines[y]) or ny < 0 or ny >= len(lines) or lines[ny][nx] != crop:
            dimensions[1] += 1


if __name__ == "__main__":
    main()
