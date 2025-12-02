"""
    # Author:   ZILNULL
    # Created:  12-2-2025

This is the second day of Advent of Code, which deals with checking various product ID
ranges in order to figure out information. Valid IDs are only the ones that do not have
any repeated sequences of numbers.

Example of valid IDs: 12345, 7263, 901934...
Example of invalid IDs: 9999, 6060, 543543...

THIS FILE CONTAINS ALL THE TESTS FOR puzzle2.py
"""

from pathlib import Path

import puzzle2


def test_check_validity():
    print("BEGINNING VALIDITY FUNCTION CHECK\n===========================")
    valid_ids = ["1", "20", "1234", "8263", "9876", "1239865243927", "678678678"]
    invalid_ids = [
        "9999",
        "1212",
        "1234512345",
        "98179817",
        "11",
        "121212121212",
        "1188511885",
    ]

    print("CHECKING CORRECT IDs: ")
    for i in valid_ids:
        valid: bool = puzzle2.check_validity(i)
        print(f"Checking {i}: {valid}")

    print("\nCHECKING INCORRECT IDs: ")
    for i in invalid_ids:
        valid: bool = puzzle2.check_validity(i)
        print(f"Checking {i}: {valid}")

    print("\n\n")
    return


def test_small_input():
    file_name = Path(__file__).parent.resolve() / "input_test.txt"
    puzzle2.solve_puzzle_part1(file_name)
    return


if __name__ == "__main__":
    test_check_validity()
    input()
    test_small_input()
