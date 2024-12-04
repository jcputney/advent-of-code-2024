import re

with open("input/3_2.txt") as f:
    contents = f.read()
    regex = r"mul\s*\(\s*(\d{1,3}),\s*(\d{1,3})\s*\)"
    results = []
    pos = 0
    enabled = True

    while match := re.search(regex, contents[pos:]):
        match_pos = pos + match.start()
        do_pos = contents.find("do()", pos, match_pos)
        dont_pos = contents.find("don't()", pos, match_pos)
        if 0 < do_pos < match_pos:
            enabled = True
        elif 0 < dont_pos < match_pos:
            enabled = False

        if enabled:
            results.append(match.groups())

        pos += match.end()

    print(sum(int(x) * int(y) for x, y in results))
