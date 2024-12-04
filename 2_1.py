if __name__ == '__main__':
    with open('input/2_1.txt', 'r') as file:
        reports = [list(map(int, report.strip().split())) for report in file.readlines()]
        safe_count = 0

        for report in reports:
            increasing = None
            for i in range(len(report) - 1):
                diff = report[i] - report[i + 1]
                if diff == 0 or abs(diff) > 3 or (increasing is not None and (diff > 0) != increasing):
                    break
                increasing = diff > 0
            else:
                safe_count += 1

        print(safe_count)
