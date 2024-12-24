import time

MASK_24 = (1 << 24) - 1  # 24-bit mask


class PuzzleSolver:
    def __init__(self, secret_input: int):
        self.secret = secret_input & MASK_24

    def evolve(self):
        self.secret ^= ((self.secret << 6) & MASK_24)
        self.secret ^= (self.secret >> 5)
        self.secret &= MASK_24
        self.secret ^= ((self.secret << 11) & MASK_24)
        self.secret &= MASK_24

    def solve(self, iterations: int) -> int:
        for _ in range(iterations):
            self.evolve()
        return self.secret


if __name__ == "__main__":
    with open("input/22_1.txt", "r") as f:
        secrets = list(map(int, f.read().splitlines()))

    evolutions = 2000

    start_time = time.time()
    total = 0
    for secret in secrets:
        solver = PuzzleSolver(secret)
        total += solver.solve(evolutions)

    elapsed = time.time() - start_time
    print(f"Result is {total}")
    print(f"Time taken: {elapsed:.3f} seconds")
