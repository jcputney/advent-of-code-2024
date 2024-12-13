def main():
    with open('input/12_2.txt') as f:
        lines = f.read().splitlines()

    visited = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]

    total = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if not visited[y][x]:
                crop = lines[y][x]
                region_cells = []
                dfs_region(x, y, crop, lines, visited, region_cells)

                area = len(region_cells)
                corners = count_corners(region_cells)

                price = area * corners
                print(f"A region of `{crop}` plants with price {area} * {corners} = {price}")
                total += price

    print(total)


def dfs_region(x, y, crop, lines, visited, region_cells):
    stack = [(x, y)]
    visited[y][x] = True

    while stack:
        cx, cy = stack.pop()
        region_cells.append((cx, cy))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= ny < len(lines) and 0 <= nx < len(lines[0]) and not visited[ny][nx] and \
                    lines[ny][nx] == crop:
                visited[ny][nx] = True
                stack.append((nx, ny))


def count_corners(region_cells):
    region_set = set(region_cells)
    corners = 0

    for x, y in region_set:
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for i, (dx, dy) in enumerate(directions):
            nx, ny = (x + dx, y + dy)
            cw = directions[(i + 1) % 4]  # Clockwise
            ax, ay = (x + dx + cw[0], y + dy + cw[1])

            if (nx, ny) not in region_set and (
                    (x + cw[0], y + cw[1]) not in region_set or (ax, ay) in region_set):
                corners += 1

    return corners


if __name__ == "__main__":
    main()
