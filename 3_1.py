import re
with open("input/3_1.txt") as f:
    contents = f.read()
    regex = r"mul\s*\(\s*(\d{1,3}),\s*(\d{1,3})\s*\)"
    results = re.findall(regex, contents)
    total = 0

    for result in results:
        total += int(result[0]) * int(result[1])

    print(total)
