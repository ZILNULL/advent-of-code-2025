"""
    # Author:   ZILNULL
    # Created:  12-1-2025

This is the first puzzle of the AoC 2025 challenge. The objective is as follows:
Find the password given a certain input. The input consists of rotations performed
on the dial of a safe (L50, R20, etc.)

Part 1:
    The password is equal to the amount of times the dial's arrow has landed on 0
    after finishing any given rotation.

Part 2:
    The password is equal to the amount of times the dial's arrow has passed through
    the number 0.
"""

from pathlib import Path


def change_value(curr_num: int, change_val: int) -> int:
    """
    Keep the value of the dial within the range of 0-99.
    """
    new_num: int = (curr_num + change_val) % 100
    return new_num


def count_zero_clicks(curr_num: int, change_val: int) -> tuple[int, int]:
    """
    Count the amount of times that zero has been clicked in a given rotation.
    """
    new_num: int = curr_num + change_val
    zero_clicks: int = abs(int(new_num / 100))

    if (curr_num > 0 and new_num < 0) or new_num == 0:
        zero_clicks += 1

    return (new_num % 100, zero_clicks)


def parse_input(input_line: str) -> int:
    """
    Parse each input line to turn it into a signed number depending on direction.
    """
    input_line_clean: str = input_line.strip().strip("\n")
    direction: str = input_line_clean[0].lower()
    number: int = int(input_line_clean[1:])

    if direction == "l":
        number = number * -1

    return number


def solve_puzzle_part1(file: Path) -> int:
    with open(file, "r") as f:
        inputs: list[str] = f.readlines()

    zero_count: int = 0
    curr_num: int = 50
    for input in inputs:
        change_val: int = parse_input(input)
        curr_num = change_value(curr_num, change_val)

        if curr_num == 0:
            zero_count += 1

    return zero_count


def solve_puzzle_part2(file: Path) -> int:
    with open(file, "r") as f:
        inputs: list[str] = f.readlines()

    zero_clicks: int = 0
    zero_count: int = 0
    curr_num: int = 50
    for input in inputs:
        change_val: int = parse_input(input)
        curr_num, zero_clicks = count_zero_clicks(curr_num, change_val)
        zero_count += zero_clicks

    return zero_count


def solver_picker(file: Path) -> int:
    option = input("Which part do you want to solve? (1 | 2): ")
    solution: int = 0

    match option:
        case "1":
            solution = solve_puzzle_part1(file)
        case "2":
            solution = solve_puzzle_part2(file)
        case _:
            return -1

    return solution


def main():
    file_input: Path = Path(__file__).parent.resolve() / "input.txt"
    password: int = solver_picker(file_input)
    print(f"The password is {password}!")
    return 0


if __name__ == "__main__":
    _ = main()
