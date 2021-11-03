import hashlib
import itertools


def main():
    inputs = open("inputs/day04.txt", 'r').read().strip()
    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def part_one(inputs: str) -> int:
    for i in itertools.count(start=1):
        digest = hashlib.md5(f"{inputs}{i}".encode()).hexdigest()

        if str(digest).startswith("00000"):
            return i


def part_two(inputs: str) -> int:
    for i in itertools.count(start=1):
        digest = hashlib.md5(f"{inputs}{i}".encode()).hexdigest()

        if str(digest).startswith("000000"):
            return i


if __name__ == '__main__':
    main()
