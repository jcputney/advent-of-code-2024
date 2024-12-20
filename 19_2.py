import time

memo = {}

def check(patterns: list[str], design: str) -> int:
    if design in memo:
        return memo[design]

    if not design:
        memo[design] = 1
        return 1

    total_count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            remainder = design[len(pattern):]
            total_count += check(patterns, remainder)

    memo[design] = total_count
    return total_count


def main():
    before = time.perf_counter()

    with open('input/19_2.txt') as f:
        patterns_block, designs_block = f.read().split("\n\n")

    patterns = set(patterns_block.strip().split(", "))
    designs = designs_block.strip().split("\n")

    sorted_patterns = sorted(patterns, key=lambda x: len(x), reverse=True)

    # Pre-warm the memo by checking all patterns themselves
    for pattern in sorted_patterns:
        check(sorted_patterns, pattern)

    possible_count = 0
    all_counts = {}

    for design in designs:
        count = check(sorted_patterns, design)
        if count > 0:
            all_counts[design] = count
            possible_count += count

    print("Total Possible Designs:", possible_count)

    print(f"Time taken: {time.perf_counter() - before:.4f}s")


if __name__ == "__main__":
    main()
