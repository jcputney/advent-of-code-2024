import re

if __name__ == '__main__':
    with open('input/1_2.txt', 'r') as file:
        lines = file.readlines()
        left = []
        right = []
        for line in lines:
            row = re.split(r'\s+', line)
            left.append(row[0])
            right.append(row[1])
        left = sorted(left)
        right = sorted(right)

        similarity = 0
        right_index = 0
        score_cache = {}
        for i in range(len(left)):
            left_value = int(left[i])
            if left_value in score_cache:
                similarity += score_cache[left_value]
                continue

            current_score = 0
            right_value = int(right[right_index])
            while left_value >= right_value:
                if left_value == right_value:
                    current_score += 1
                right_index += 1
                if right_index == len(right):
                    break
                right_value = int(right[right_index])

            score_cache[left_value] = current_score * left_value
            similarity += current_score * left_value

        print(similarity)
