import re
from typing import Iterable


class Instruction(object):
    def __init__(self, line: str):
        matches = re.search(r"(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)", line)
        op, start, stop = matches.groups()

        self.op = op
        self.start = Instruction._parse_pos(start)
        self.stop = Instruction._parse_pos(stop)

    def iterate(self) -> Iterable[tuple[int, int]]:
        for y in range(self.start[1], self.stop[1] + 1):
            for x in range(self.start[0], self.stop[0] + 1):
                yield x, y

    @staticmethod
    def _parse_pos(val: str) -> (int, int):
        sp = val.split(",", 1)
        return int(sp[0]), int(sp[1])


def main():
    inputs = [Instruction(i) for i in open("inputs/day06.txt", 'r').readlines()]
    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def part_one(inputs: list[Instruction]) -> int:
    grid = [[False] * 1000 for _ in range(1000)]

    for i in inputs:
        for x, y in i.iterate():
            if i.op == "toggle":
                grid[x][y] = not grid[x][y]
            else:
                grid[x][y] = i.op == "turn on"

    return sum([sum(i) for i in grid])


def part_two(inputs: list[Instruction]) -> int:
    grid = [[0] * 1000 for _ in range(1000)]

    for i in inputs:
        for x, y in i.iterate():
            if i.op == "turn on":
                grid[x][y] += 1
            elif i.op == "toggle":
                grid[x][y] += 2
            elif i.op == "turn off":
                grid[x][y] = max(0, grid[x][y] - 1)

    return sum([sum(i) for i in grid])


if __name__ == '__main__':
    main()
