def main():
    blink_count = 25

    with open('input/11_1.txt') as f:
        stones = list(map(int, f.read().splitlines()[0].split()))

    stone_counts = {}
    for stone in stones:
        if stone not in stone_counts:
            stone_counts[stone] = 0
        stone_counts[stone] += 1

    for _ in range(blink_count):
        for stone, count in {stone: count for stone, count in stone_counts.items() if count > 0}.items():
            for _ in range(count):
                stone_counts[stone] -= 1
                if stone == 0:
                    if 1 not in stone_counts:
                        stone_counts[1] = 0
                    stone_counts[1] += 1
                elif len(str(stone)) % 2 == 0:
                    half = len(str(stone)) // 2
                    left = int(str(stone)[:half])
                    right = int(str(stone)[half:])

                    if left not in stone_counts:
                        stone_counts[left] = 0
                    stone_counts[left] += 1
                    if right not in stone_counts:
                        stone_counts[right] = 0
                    stone_counts[right] += 1
                else:
                    multiple = stone * 2024
                    if multiple not in stone_counts:
                        stone_counts[multiple] = 0
                    stone_counts[multiple] += 1

    total = sum([count for count in stone_counts.values()])

    print(total)


if __name__ == "__main__":
    main()
