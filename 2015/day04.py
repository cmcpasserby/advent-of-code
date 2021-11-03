import hashlib
import itertools


def main():
    inputs = open("inputs/day04.txt", 'r').read().strip()
    part_one(inputs)
    part_two(inputs)


def part_one(inputs: str):
    for i in itertools.count(start=1):
        digest = hashlib.md5(f"{inputs}{i}".encode()).hexdigest()

        if str(digest).startswith("00000"):
            print(f"Part One: {i}")
            return


def part_two(inputs: str):
    for i in itertools.count(start=1):
        digest = hashlib.md5(f"{inputs}{i}".encode()).hexdigest()

        if str(digest).startswith("000000"):
            print(f"Part Two: {i}")
            return


if __name__ == '__main__':
    main()
