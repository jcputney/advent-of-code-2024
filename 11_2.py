import pandas as pd

def main():
    blink_count = 75

    with open('input/11_2.txt') as f:
        stones = list(map(int, f.read().splitlines()[0].split()))

    stone_counts = pd.Series(stones).value_counts().to_dict()

    for _ in range(blink_count):
        new_counts = {}
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] = new_counts.get(1, 0) + count
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                left = int(str(stone)[:half])
                right = int(str(stone)[half:])
                new_counts[left] = new_counts.get(left, 0) + count
                new_counts[right] = new_counts.get(right, 0) + count
            else:
                multiple = stone * 2024
                new_counts[multiple] = new_counts.get(multiple, 0) + count
        stone_counts = new_counts

    total = sum(stone_counts.values())
    print(total)

if __name__ == "__main__":
    main()
