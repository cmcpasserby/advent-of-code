from math import prod


def main():
    inputs = [tuple(int(n) for n in i.split("x", 2)) for i in open("inputs/day02.txt", 'r').readlines()]
    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def part_one(inputs: list[tuple[int, ...]]) -> int:
    return sum(get_area(i) for i in inputs)


def part_two(inputs: list[tuple[int, ...]]) -> int:
    return sum(get_bow_length(i) for i in inputs)


def get_area(sides: tuple[int, ...]) -> int:
    l, w, h = sides
    sides = 2*l*w, 2*w*h, 2*h*l
    return sum(sides) + min(sides) // 2


def get_bow_length(sides: tuple[int, ...]) -> int:
    a, b, _ = sorted(sides)
    to_wrap = a * 2 + b * 2
    bow = prod(sides)
    return to_wrap + bow


if __name__ == '__main__':
    main()
