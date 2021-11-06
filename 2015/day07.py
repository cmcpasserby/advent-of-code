import operator

from typing import Callable

mon_ops: dict[str, Callable[[int], int]] = {
    "NOT": lambda x: ~x & 0xffff
}

bin_ops: dict[str, Callable[[int, int], int]] = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}


class Instruction(object):
    def __init__(self, s: str):
        pass


def main():
    inputs = [Instruction(i) for i in open("inputs/day07.txt", 'r').readlines()]


def part_one() -> int:
    pass


def part_two() -> int:
    pass


if __name__ == '__main__':
    main()
