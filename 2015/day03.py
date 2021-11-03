from collections import defaultdict


dir_map = {">": 1, "<": -1, "^": 1j, "v": -1j}


def main():
    inputs = [dir_map[i] for i in open("inputs/day03.txt", 'r').read()]
    part_one(inputs)
    part_two(inputs)


def part_one(inputs: list[complex]):
    grid: dict[complex, int] = defaultdict(int)

    grid[0] += 1
    pointer = 0

    for direction in inputs:
        pointer += direction
        grid[pointer] += 1

    result = sum(i > 0 for i in grid.values())
    print(f"Part One: {result}")


def part_two(inputs: list[complex]):
    grid: dict[complex, int] = defaultdict(int)

    santa_inputs = inputs[0:][::2]
    grid[0] += 1
    pointer = 0
    for direction in santa_inputs:
        pointer += direction
        grid[pointer] += 1

    elf_inputs = inputs[1:][::2]
    grid[0] += 1
    pointer = 0
    for direction in elf_inputs:
        pointer += direction
        grid[pointer] += 1

    result = sum(i > 0 for i in grid.values())
    print(f"Part Two: {result}")


if __name__ == '__main__':
    main()
