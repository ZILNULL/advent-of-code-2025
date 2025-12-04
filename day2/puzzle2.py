"""
    # Author:   ZILNULL
    # Created:  12-2-2025

This is the second day of Advent of Code, which deals with checking various product ID
ranges in order to figure out information. Valid IDs are only the ones that do not have
any sequence of digits that is repeated twice.

Example of valid IDs: 12345, 7263, 901934, 111...
Example of invalid IDs: 9999, 6060, 543543, 11...

Part 1:
    Find all the invalid IDs and find their combined sum.

Part 2:
    Now, it will be considered in valid if the sequence of digits is repeated any
    given number of twice. For example, 111 would be invalid.
"""

from pathlib import Path


def split_string_by_length(s: str, l: int) -> list[str]:
    """
    Takes any given string and splits it in chunks of maximum l length.
    """
    chunks: list[str] = [s[i : i + l] for i in range(0, len(s), l)]
    return chunks


def check_validity_part1(prod_id: str) -> bool:
    """
    This function checks whether a given id is entirely made up of a repeating
    sequence of characters or not. Only checks if the sequence repeats twice.
    """
    length: int = len(prod_id)
    half: int = int(length / 2)
    valid: bool = (length % 2 == 1) or (prod_id[0:half] != prod_id[half:length])
    return valid


def check_validity_part2(prod_id: str) -> bool:
    """
    Same as check_validity_part1, but checks for any arbitrary number of repeats.
    """
    length: int = len(prod_id)
    half: int = int(length / 2)
    if length == 1:
        return True

    valid = True
    for i in range(half):
        seq_idx = length - 1 - i
        if prod_id[0] != prod_id[seq_idx]:
            continue

        sub_seq = split_string_by_length(prod_id, i + 1)
        if len(set(sub_seq)) == 1:
            valid = False
            break

    return valid


def obtain_range_limits(range_str: str) -> tuple[int, int]:
    """
    Obtain the minimum and maximum number (of a range given a sequence of characters
    X-Y, where both X and Y are included.
    """
    limits: list[str] = range_str.split("-")
    min: int = int(limits[0])
    max: int = int(limits[1])
    return (min, max)


def obtain_all_nums(min: int, max: int) -> list[str]:
    """
    Obtain all the numbers in a given range, casted to string for character comparison.
    """
    nums: list[int] = list(range(min, max + 1))
    nums_str: list[str] = [str(x) for x in nums]
    return nums_str


def read_input(file: Path) -> list[str]:
    with open(file, "r") as f:
        lines: list[str] = f.readlines()

    input: list[str] = lines[0].split(",")
    return input


def solve_puzzle_part1(file: Path) -> int:
    ranges: list[str] = read_input(file)

    total: int = 0
    for r in ranges:
        r_min, r_max = obtain_range_limits(r)
        nums = obtain_all_nums(r_min, r_max)

        for n in nums:
            if not check_validity_part2(n):
                total += int(n)

    print(f"The total of every invalid ID is: {total}")
    return total


def main():
    file_name = Path(__file__).parent.resolve() / "input.txt"
    _ = solve_puzzle_part1(file_name)
    return 0


if __name__ == "__main__":
    _ = main()
