def main():
    inputs = open("inputs/day01.txt", 'r').read()

    part_one(inputs)
    part_two(inputs)


def part_one(inputs: str):
    count = sum(1 if c == '(' else -1 for c in inputs)
    print(f"Part One: {count}")


def part_two(inputs: str):
    count = 0

    for i, c in enumerate(inputs):
        count += 1 if c == '(' else -1
        if count < 0:
            print(f"Part Two: {i + 1}")
            break


if __name__ == '__main__':
    main()
