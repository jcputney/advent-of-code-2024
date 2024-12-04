import re

if __name__ == '__main__':
    with open('input/1_1.txt', 'r') as file:
        lines = file.readlines()
        left = []
        right = []
        for line in lines:
            row = re.split(r'\s+', line)
            left.append(row[0])
            right.append(row[1])
        left = sorted(left)
        right = sorted(right)

        distance = 0
        for i in range(len(left)):
            distance += abs(int(left[i]) - int(right[i]))

        print(distance)
