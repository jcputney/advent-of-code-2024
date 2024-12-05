import re


def check_valid_update(rules, update):
    for rule in rules:
        if rule[0] in update:
            if rule[1] in update and update.index(rule[1]) < update.index(rule[0]):
                return False
    return True


def main():
    with open("input/5_2.txt") as f:
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
            if not check_valid_update(rules, update):
                while not check_valid_update(rules, update):
                    for rule in rules:
                        if rule[0] not in update or rule[1] not in update:
                            continue
                        left_index = update.index(rule[0])
                        right_index = update.index(rule[1])
                        if right_index < left_index:
                            update[left_index], update[right_index] = update[right_index], update[left_index]

                middle_total += update[int(len(update) / 2)]

        print("Middle Total: ", middle_total)


if __name__ == "__main__":
    main()
