import itertools
import re

import numpy as np


class PuzzleSolver:
    def __init__(self, codes: list[str]):
        self.codes = codes

        self.loc_x = {
            '7': 0, '8': 0, '9': 0,
            '4': 1, '5': 1, '6': 1,
            '1': 2, '2': 2, '3': 2,
            '#': 3, '^': 3, 'A': 3,
            '<': 4, 'v': 4, '>': 4,
        }
        self.loc_y = {
            '7': 0, '8': 1, '9': 2,
            '4': 0, '5': 1, '6': 2,
            '1': 0, '2': 1, '3': 2,
            '#': 0, '^': 1, 'A': 2,
            '<': 0, 'v': 1, '>': 2,
        }

        self.options = 'A^<v>'
        self.pairs = [x + y for (x, y) in itertools.product(self.options, self.options)]
        self.N = len(self.pairs)

        self.matrix = np.zeros((self.N, self.N), dtype=object)

        self.build_matrix()

    def best_path(self, x1: int, y1: int, x2: int, y2: int) -> str:
        lt = '<' * (y1 - y2)
        rt = '>' * (y2 - y1)
        up = '^' * (x1 - x2)
        dn = 'v' * (x2 - x1)

        if self.loc_x['#'] == min(x1, x2) and self.loc_y['#'] == min(y1, y2):
            return dn + rt + up + lt + "A"
        elif self.loc_x['#'] == max(x1, x2) and self.loc_y['#'] == min(y1, y2):
            return up + rt + dn + lt + "A"
        else:
            return lt + dn + up + rt + "A"

    def build_matrix(self):
        for src_idx, pair in enumerate(self.pairs):
            a, b = pair[0], pair[1]
            # best_path from char a -> b
            path = self.best_path(
                self.loc_x[a], self.loc_y[a],
                self.loc_x[b], self.loc_y[b]
            )
            for (c1, c2) in zip('A' + path, path):
                # find index of the 2-char pair (c1+c2)
                dest_idx = self.pairs.index(c1 + c2)
                self.matrix[src_idx, dest_idx] += 1

    def fastest_pairs(self, depth: int) -> np.ndarray:
        vect = np.ones(self.N, dtype=object)
        mat_power = np.linalg.matrix_power(self.matrix, depth)
        return mat_power.dot(vect)

    def fastest_string(self, s: str, fp: np.ndarray) -> int:
        return sum(fp[self.pairs.index(a + b)] for (a, b) in zip("A" + s, s))

    def solve_for_code(self, code: str, depth: int) -> int:
        code = code.replace('0', '^')
        if depth == 0:
            return len(code)

        fp = self.fastest_pairs(depth - 1)

        result = 0
        for (c1, c2) in zip("A" + code, code):
            local_path = self.best_path(
                self.loc_x[c1], self.loc_y[c1],
                self.loc_x[c2], self.loc_y[c2]
            )
            result += self.fastest_string(local_path, fp)
        return result

    def solve(self, depth: int) -> int:
        total = 0
        for code in self.codes:
            num_part = re.findall(r'\d+', code)
            if not num_part:
                continue
            numeric_value = int(num_part[0])

            cost_for_code = self.solve_for_code(code, depth)
            total += cost_for_code * numeric_value
        return total


if __name__ == "__main__":
    with open("input/21_1.txt", "r") as f:
        input_codes = f.read().splitlines()

    solver = PuzzleSolver(input_codes)

    print(f"Result is {solver.solve(26)}")
