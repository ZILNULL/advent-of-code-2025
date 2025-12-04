"""
    # Author:   ZILNULL
    # Created:  12-4-2025

This is the third day of the advent of code, where the puzzle consists of activating various batteries in battery banks.

Part 1:
    We have to activate exactly two batteries in each bank.
    The two batteries that have to be activated in each bank are the ones that
    provide the largest amount of joltage possible. Calculate the total joltage.

Part 2:
    Instead of two, now we have to use 12 batteries.
"""

from pathlib import Path
from typing import cast


def combine_joltage_bank(batteries: list[int]) -> int:
    val_joltage: int = 0
    for i in range(len(batteries)):
        val_joltage += batteries[-1 - i] * cast(int, 10**i)

    return val_joltage


def find_max_value_sequence(line: str) -> tuple[int, int]:
    joltages: list[int] = [int(c) for c in line]
    max_joltage: tuple[int, int] = (0, 0)
    for i, n in enumerate(joltages):
        if n == 9:
            max_joltage = (i, n)
            break

        if n > max_joltage[1]:
            max_joltage = (i, n)

    return max_joltage


def find_max_batteries(line: str, num_batteries: int) -> list[int]:
    batteries_idx: list[int] = [0 for _ in range(num_batteries)]
    batteries_val: list[int] = [0 for _ in range(num_batteries)]
    bank_length: int = len(line)
    for i in range(num_batteries):
        min_position = 0 if i == 0 else batteries_idx[i - 1] + 1
        max_position = bank_length - (num_batteries - i)
        max_joltage = find_max_value_sequence(line[min_position:max_position])

        batteries_idx[i] = max_joltage[0] + min_position
        batteries_val[i] = max_joltage[1]

    return batteries_val


def solve_puzzle_part1(file: Path) -> int:
    with open(file, "r") as f:
        lines = f.readlines()

    joltages_banks: list[int] = []
    for line in lines:
        batteries_val = find_max_batteries(line, 2)
        joltage = combine_joltage_bank(batteries_val)
        joltages_banks.append(joltage)

    return sum(joltages_banks)


def solve_puzzle_part2(file: Path) -> int:
    with open(file, "r") as f:
        lines = f.readlines()

    joltages_banks: list[int] = []
    for line in lines:
        batteries_val = find_max_batteries(line, 12)
        joltage = combine_joltage_bank(batteries_val)
        joltages_banks.append(joltage)

    return sum(joltages_banks)


def main():
    file = Path(__file__).parent.resolve() / "input.txt"
    option = input("Which part do you want to solve? (1 | 2): ")
    solution: int = 0

    match option:
        case "1":
            solution = solve_puzzle_part1(file)
        case "2":
            solution = solve_puzzle_part2(file)
        case _:
            return -1

    print(f"The solution is {solution}.")
    return 0


if __name__ == "__main__":
    _ = main()
