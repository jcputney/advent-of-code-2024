import time


def check(patterns: list[str], design: str, current_pattern="", new_patterns=None,
          visited=None) -> (bool, list[str]):
    if new_patterns is None:
        new_patterns = []
    if visited is None:
        visited = set()
    if design in visited:
        return False, new_patterns
    visited.add(design)

    for pattern in [p for p in patterns if len(p) <= len(design) and p[0] == design[0]]:
        working_design = design
        if working_design.startswith(pattern):
            current_pattern += pattern
            new_patterns.append(current_pattern)
            working_design = working_design.replace(pattern, "", 1)
            if not working_design:
                return True, new_patterns
            found, current_patterns = check(patterns, working_design, current_pattern, new_patterns,
                                            visited)
            if found:
                return True, current_patterns
    return False, new_patterns


def main():
    before = time.perf_counter()

    with open('input/19_1.txt') as f:
        patterns, designs = f.read().split("\n\n")

    patterns = set(patterns.strip().split(", "))
    designs = designs.strip().split("\n")

    print(patterns)
    print(designs)

    possible_count = 0
    for design in designs:
        found, new_patterns = check(sorted(patterns, key=lambda x: len(x), reverse=True), design)
        if new_patterns:
            patterns.union(new_patterns)
        if found:
            patterns.add(design)
            possible_count += 1

    print("Possible designs:", possible_count)
    print(f"Time taken: {time.perf_counter() - before:.2f}s")


if __name__ == "__main__":
    main()
