with open("input/2_2.txt") as f:
    reports = [list(map(int, line.split())) for line in f]


def is_safe(report: list, ignore_idx: int) -> bool:
    descending = False
    ascending = False
    previous = None

    for idx, level in enumerate(report):
        if idx == ignore_idx:
            continue

        if not previous:
            previous = level
            continue

        if previous < level:
            ascending = True
        elif previous > level:
            descending = True

        if (previous == level) or abs(previous - level) > 3 or (ascending and descending):
            return False

        previous = level
    return True


safe_reports = sum(any(is_safe(report, i) for i in range(len(report))) for report in reports)
print(safe_reports)
