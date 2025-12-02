"""
    # Author:   ZILNULL
    # Created:  12-2-2025

This is the second day of Advent of Code, which deals with checking various product ID
ranges in order to figure out information. Valid IDs are only the ones that do not have
any repeated sequences of numbers.

Example of valid IDs: 12345, 7263, 901934...
Example of invalid IDs: 9999, 6060, 543543...

Part 1:
    Find all the invalid IDs and find their combined sum.
"""

from pathlib import Path
from typing import List, Tuple


def check_validity(prod_id: str) -> bool:
    """
    This function checks whether a given id is entirely made up of a repeating
    sequence of characters or not.
    """
    length: int = len(prod_id)
    half: int = int(length / 2)
    valid: bool = (length % 2 == 1) or (prod_id[0:half] != prod_id[half:length])
    return valid


def obtain_range_limits(range_str: str) -> Tuple[int, int]:
    """
    Obtain the minimum and maximum number of a range given a sequence of characters
    X-Y, where both X and Y are included.
    """
    limits: List[str] = range_str.split("-")
    min: int = int(limits[0])
    max: int = int(limits[1])
    return (min, max)


def obtain_all_nums(min: int, max: int) -> List[str]:
    """
    Obtain all the numbers in a given range, casted to string for character comparison.
    """
    nums: List[int] = list(range(min, max + 1))
    nums_str: List[str] = [str(x) for x in nums]
    return nums_str


def read_input(file: Path) -> List[str]:
    with open(file, "r") as f:
        lines: List[str] = f.readlines()

    input: List[str] = lines[0].split(",")
    return input


def solve_puzzle_part1(file: Path) -> int:
    ranges: List[str] = read_input(file)

    total: int = 0
    for r in ranges:
        r_min, r_max = obtain_range_limits(r)
        nums = obtain_all_nums(r_min, r_max)

        for n in nums:
            if not check_validity(n):
                total += int(n)

    print(f"The total of every invalid ID is: {total}")
    return total


def main():
    file_name = Path(__file__).parent.resolve() / "input.txt"
    solve_puzzle_part1(file_name)
    return 0


if __name__ == "__main__":
    main()
