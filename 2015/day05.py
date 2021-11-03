import re
from itertools import islice
from typing import Iterable

def main():
    inputs = open("inputs/day05.txt", 'r').readlines()
    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def part_one(inputs: list[str]) -> int:
    def test(word: str) -> bool:
        return bool(
            re.search(r'.*([aeiou].*){3}', word)
            and re.search(r'(.)\1', word)
            and not re.search(r'(ab|cd|pq|xy)', word)
        )
    return sum(test(i) for i in inputs)


def part_two(inputs: list[str]) -> int:
    def test(word: str) -> bool:
        return bool(re.search(r'(..).*\1', word) and re.search(r'(.).\1', word))
    return sum(test(i) for i in inputs)


def window(seq: str, n: int = 2) -> Iterable[tuple[str, ...]]:
    it = iter(seq)
    result = tuple(islice(it, n))

    if len(result) == n:
        yield result

    for elem in it:
        result = result[1:] + (elem,)
        yield result


if __name__ == '__main__':
    main()
