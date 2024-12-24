import time
from collections import defaultdict

MASK_24 = (1 << 24) - 1  # 24-bit mask == secret % 16777216


class SecretSolver:
    def __init__(self, secret: int):
        self.secret = secret & MASK_24
        self.prices = [self.secret % 10]

    def evolve(self):
        self.secret ^= ((self.secret << 6) & MASK_24)
        self.secret ^= (self.secret >> 5)
        self.secret &= MASK_24
        self.secret ^= ((self.secret << 11) & MASK_24)
        self.secret &= MASK_24


    def generate_prices(self, iterations: int):
        for _ in range(iterations):
            self.evolve()
            self.prices.append(self.secret % 10)


    def first_occurrences_of_diffs(self) -> dict[tuple[int, int, int, int], int]:
        diffs = []
        for i in range(len(self.prices) - 1):
            diffs.append(self.prices[i + 1] - self.prices[i])

        pattern_earliest = {}

        # We need at least 4 diffs to form a pattern
        for i in range(len(diffs) - 3):
            pattern = (diffs[i], diffs[i + 1], diffs[i + 2], diffs[i + 3])
            if pattern not in pattern_earliest:  # only record the first time
                # sell price is the price AFTER these 4 diffs -> prices[i+4]
                pattern_earliest[pattern] = self.prices[i + 4]
        return pattern_earliest


def main():
    with open("input/22_2.txt", "r") as f:
        secrets = list(map(int, f.read().splitlines()))

    evolutions = 2000

    total_for_pattern = defaultdict(int)

    start_time = time.time()

    for secret in secrets:
        solver = SecretSolver(secret)
        # Generate prices for each secret
        solver.generate_prices(evolutions)
        # Find the earliest occurrence of each 4-diff pattern
        earliest = solver.first_occurrences_of_diffs()
        for pattern, sell_price in earliest.items():
            total_for_pattern[pattern] += sell_price

    # Find the pattern with the max total bananas
    best_pattern, best_sum = None, 0
    for pattern, current_sum in total_for_pattern.items():
        if current_sum > best_sum:
            best_sum = current_sum
            best_pattern = pattern

    elapsed = time.time() - start_time

    print(f"Best 4-diff pattern: {best_pattern}")
    print(f"Max bananas total  : {best_sum}")
    print(f"Time elapsed       : {elapsed:.3f} s")


if __name__ == "__main__":
    main()
