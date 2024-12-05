import re

with open("input/5_1.txt") as f:
    lines = f.read().splitlines()

    rules = []
    updates = []

    rule_regex = r"\d+\|\d+"

    for line in lines:
        if re.match(rule_regex, line):
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    middle_total = 0
    for update in updates:
        # the number on the left side of the rule must appear in the update before the number on the right side of the rule
        valid = True
        for rule in rules:
            if rule[0] in update:
                # if right side is in update but index is less than left side index, invalid
                if rule[1] in update and update.index(rule[1]) < update.index(rule[0]):
                    valid = False
                    break
        if valid:
            middle_total += update[int(len(update) / 2)]
            # print("Valid update: ", update)

    print("Middle Total: ", middle_total)
