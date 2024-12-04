with open("input/4_2.txt") as f:
    lines = f.read().splitlines()

    count = 0

    search = 'MAS'
    for line_num in range(1, len(lines) - 1):
        for line_pos in range(1, len(lines[line_num]) - 1):
            if lines[line_num][line_pos] == 'A':
                left_diag = lines[line_num - 1][line_pos - 1] + 'A' + lines[line_num + 1][line_pos + 1]
                right_diag = lines[line_num + 1][line_pos - 1] + 'A' + lines[line_num - 1][line_pos + 1]
                if (left_diag == search or left_diag[::-1] == search) and (right_diag == search or right_diag[::-1] == search):
                    count += 1

    print(count)
