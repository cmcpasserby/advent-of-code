def main():
    inputs = open("inputs/day01.txt", 'r').read()

    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def part_one(inputs: str) -> int:
    return sum(1 if c == '(' else -1 for c in inputs)


def part_two(inputs: str) -> int:
    count = 0

    for i, c in enumerate(inputs):
        count += 1 if c == '(' else -1
        if count < 0:
            return i + 1


if __name__ == '__main__':
    main()
