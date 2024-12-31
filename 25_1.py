import time
from typing_extensions import Self


class LockAndKey:
    def __init__(self, key):
        lines = key.splitlines()
        self.heights = [0, 0, 0, 0, 0]
        self.is_lock = lines[0][0] == "#"
        for i, row in enumerate(lines):
            if i == 0 or i == len(lines) - 1:
                continue
            for j, char in enumerate(row):
                if char == "#":
                    self.heights[j] += 1

    def __str__(self):
        return f"{'Lock' if self.is_lock else 'Key'}: {self.heights}"

    def fits(self, lock_or_key: Self) -> bool:
        for i in range(5):
            if self.heights[i] + lock_or_key.heights[i] > 5:
                return False
        return True


def main():
    with open("input/25_1.txt", "r") as f:
        keys_or_locks = f.read().split("\n\n")

    keys_or_locks = [LockAndKey(item) for item in keys_or_locks]
    locks = [item for item in keys_or_locks if item.is_lock]
    keys = [item for item in keys_or_locks if not item.is_lock]

    fit_count = 0
    for lock in locks:
        for key in keys:
            if lock.fits(key):
                print(f"Key fits lock: {key} - {lock}")
                fit_count += 1

    print(f"Fit count         : {fit_count}")
    start_time = time.perf_counter()

    print(f"Time elapsed       : {time.perf_counter() - start_time :.3f} s")


if __name__ == "__main__":
    main()
