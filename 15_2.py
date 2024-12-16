DIRECTIONS = {
    '^': -1j,
    'v': 1j,
    '<': -1,
    '>': 1
}


def get_coord(position):
    return int(position.imag) * 100 + int(position.real)


class Warehouse:
    def __init__(self, grid_text, moves):
        self.robot = None
        self.moves = "".join(moves.split())

        self.grid = {}
        grid_text = grid_text.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@",
                                                                                               "@.")
        grid_lines = grid_text.split("\n")
        self.width = len(grid_lines[0])
        self.height = len(grid_lines)
        for y, row in enumerate(grid_lines):
            for x, cell in enumerate(row):
                location = x + y * 1j
                self.grid[location] = cell
                if cell == "@":
                    self.robot = location

    def print_state(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.grid.get(j + i * 1j, " "), end="")
            print()
        print()

    def perform_move(self, move):
        if self.grid[self.robot + move] == "#":
            return self.robot

        locations_to_push_from = [self.robot]
        boxes_to_push = []

        while any([self.grid[location + move] in "[]" for location in locations_to_push_from]):
            if any([self.grid[location + move] == "#" for location in locations_to_push_from]):
                # if we can't push the box, we can't move
                return self.robot
            new_locations_to_push_from = []
            for location in locations_to_push_from:
                boxes = []
                if self.grid[location + move] == "[":
                    boxes = [location + move]
                    if move in [1j, -1j]: # if move is vertical
                        boxes.append(location + move + 1) # if we found the left bracket, we need to add the right bracket
                elif self.grid[location + move] == "]":
                    boxes = [location + move]
                    if move in [1j, -1j]: # if move is vertical
                        boxes.append(location + move - 1) # if we found the right bracket, we need to add the left bracket
                boxes_to_push.extend(boxes)
                new_locations_to_push_from.extend(boxes)
            locations_to_push_from = new_locations_to_push_from

        # if we can't push the box, we can't move
        if any([self.grid[box + move] == "#" for box in boxes_to_push]):
            return self.robot

        new_symbols = {}
        # move the boxes
        for box in boxes_to_push:
            symbol = self.grid[box]
            new_symbols[box + move] = symbol
        # the box moved, so we need to update the grid
        for box in boxes_to_push:
            self.grid[box] = "."
        for box, symbol in new_symbols.items():
            self.grid[box] = symbol

        # move the robot
        self.grid[self.robot] = "."
        self.robot = self.robot + move
        self.grid[self.robot] = "@"
        return self.robot

    def perform_moves(self):
        for count, move in enumerate(self.moves):
            if move in DIRECTIONS:
                self.perform_move(DIRECTIONS[move])

    def total(self):
        return sum([get_coord(position) for position, cell in self.grid.items() if cell == "["])


def main():
    with open('input/15_2.txt') as f:
        grid_text, moves = f.read().split("\n\n")

    warehouse = Warehouse(grid_text, moves)
    print("Initial state:")
    warehouse.print_state()
    warehouse.perform_moves()
    print("Final state:")
    warehouse.print_state()
    print("Total:", warehouse.total())


if __name__ == "__main__":
    main()
