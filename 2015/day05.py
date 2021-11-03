from itertools import islice
from typing import Iterable

vowels = set(i for i in "aeiou")
blacklist = ["ab", "cd", "pq", "xy"]


def main():
    inputs = open("inputs/day05.txt", 'r').readlines()
    part_one(inputs)
    part_two(inputs)


def part_one(inputs: list[str]):
    def test(word: str) -> bool:
        vowel_count = 0
        has_repeat = False

        for a, b in window(word):
            if a in vowels:
                vowel_count += 1

            if a == b:
                has_repeat = True

        return vowel_count >= 3 and has_repeat and all(i not in word for i in blacklist)

    nice = sum(test(i) for i in inputs)
    print(f"Part One: {nice}")


def part_two(inputs: list[str]):
    def test(word: str) -> bool:
        triple_count = 0

        for a, b, c in window(word, n=3):
            if a == c and not a == b:
                triple_count += 1

        return triple_count > 0

    nice = sum(test(i) for i in inputs)
    print(f"Part Two: {nice}")


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
