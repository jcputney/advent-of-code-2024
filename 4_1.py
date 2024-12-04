search = 'XMAS'
length = len(search)

with open("input/4_1.txt") as f:
    lines = f.read().splitlines()
    line_length = len(lines[0])
    line_count = len(lines)

    count = 0

    for line_num, line in enumerate(lines):
        for letter_pos, letter in enumerate(line):
            if letter != 'X':
                continue

            if line_num >= length - 1:
                # perform upward search
                if search == ''.join(lines[line_num - i][letter_pos] for i in range(length)):
                    count += 1
                # perform upward left search
                if letter_pos >= length - 1:
                    if search == ''.join(lines[line_num - i][letter_pos - i] for i in range(length)):
                        count += 1
                # perform upward right search
                if letter_pos + length <= line_length:
                    if search == ''.join(lines[line_num - i][letter_pos + i] for i in range(length)):
                        count += 1

            if line_num  + length <= line_count:
                # perform downward search
                if search == ''.join(lines[line_num + i][letter_pos] for i in range(length)):
                    count += 1
                # perform downward left search
                if letter_pos >= length - 1:
                    if search == ''.join(lines[line_num + i][letter_pos - i] for i in range(length)):
                        count += 1
                # perform downward right search
                if letter_pos + length <= line_length:
                    if search == ''.join(lines[line_num + i][letter_pos + i] for i in range(length)):
                        count += 1

            # perform right search
            count += 1 if letter_pos + length <= line_length and line[letter_pos:letter_pos + length] == search else 0

            # perform left search
            count += 1 if letter_pos - length + 1 >= 0 and search == ''.join(line[letter_pos - i] for i in range(length)) else 0

    print(count)

