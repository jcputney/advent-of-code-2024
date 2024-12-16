DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def main():
    with open('input/15_1.txt') as f:
        lines = f.read().splitlines()

    boxes, walls, robot = read_input(lines)
    perform_moves(lines, walls, boxes, robot)

    total = sum(100 * x + y for x, y in boxes)
    print("Total:", total)

def push_box(x, y, dx, dy, walls, boxes):
    nx, ny = x + dx, y + dy

    # If the next position is a wall, can't push
    if (nx, ny) in walls:
        return False

    # If there's another box ahead, try pushing it first
    if (nx, ny) in boxes and not push_box(nx, ny, dx, dy, walls, boxes):
        return False

    # If we reached here, we can move the current box
    boxes.remove((x, y))
    boxes.add((nx, ny))
    return True

def move_if_possible(robot_pos, dx, dy, walls, boxes):
    nx, ny = robot_pos[0] + dx, robot_pos[1] + dy

    # If next position is a wall, can't move
    if (nx, ny) in walls:
        return robot_pos

    # If next position is free, move robot
    if (nx, ny) not in boxes:
        return nx, ny

    # Next position has a box, try pushing it recursively
    if push_box(nx, ny, dx, dy, walls, boxes):
        return nx, ny
    else:
        return robot_pos

def perform_moves(lines, walls, boxes, robot):
    for line in lines:
        for move in line:
            if move in DIRECTIONS:
                dx, dy = DIRECTIONS[move]
                robot = move_if_possible(robot, dx, dy, walls, boxes)

def read_input(lines):
    walls = set()
    boxes = set()
    robot = (-1, -1)

    line_idx = 0
    while lines:
        line = lines.pop(0)
        if line == '':
            break
        for i, c in enumerate(line):
            if c == '#':
                walls.add((line_idx, i))
            elif c == 'O':
                boxes.add((line_idx, i))
            elif c == '@':
                robot = (line_idx, i)
        line_idx += 1

    return boxes, walls, robot

if __name__ == "__main__":
    main()
