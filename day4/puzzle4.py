"""
    # Author:   ZILNULL
    # Created:  12-4-2025

This is the 4th day of the Advent of Code challenge.

Part 1:
    Counting the amount of rolls of paper that have fewer than
    4 rolls of paper in their 8 adjacent directions.

Part 2:
    Remove the rolls that can be accessed and loop through the
    process until no more rolls can be removed. Count all the removed rolls.
"""

from pathlib import Path


def print_map(map: list[list[str]]):
    for lines in map:
        print(lines)
    return


def input_to_matrix(file: Path) -> list[list[str]]:
    with open(file, "r") as f:
        lines = f.readlines()

    map: list[list[str]] = []
    for line in lines:
        line = line.strip().strip("\n")
        map_line = [c for c in line]
        map.append(map_line)

    return map


def check_valid_position(map: list[list[str]], x: int, y: int) -> bool:
    width: int = len(map[0])
    height: int = len(map)
    valid: bool = x >= 0 and x < width and y >= 0 and y < height
    return valid


def get_adjacent_positions(
    map: list[list[str]], x: int, y: int
) -> list[tuple[int, int]]:
    adjacent: list[tuple[int, int]] = []
    modifiers: list[int] = [-1, 0, 1]

    for i in modifiers:
        for j in modifiers:
            if j == 0 and i == 0:
                continue

            if check_valid_position(map, x + i, y + j):
                adjacent.append((x + i, y + j))

    return adjacent


def count_adjacent_positions(map: list[list[str]], x: int, y: int) -> int:
    count: int = 0
    adjacent: list[tuple[int, int]] = get_adjacent_positions(map, x, y)
    for pos in adjacent:
        symbol: str = map[pos[1]][pos[0]]
        if symbol == "@":
            count += 1

    return count


def solve_puzzle_part1(file: Path) -> int:
    map = input_to_matrix(file)
    _ = print_map(map)
    count: int = 0
    width: int = len(map[0])
    height: int = len(map)

    for i in range(height):
        for j in range(width):
            if map[i][j] != "@":
                continue

            num_adj = count_adjacent_positions(map, j, i)
            if num_adj < 4:
                count += 1

    return count


def solve_puzzle_part2(file: Path) -> int:
    map = input_to_matrix(file)
    _ = print_map(map)
    count: int = 0
    started: bool = False
    count_loop: int = 0
    remove_pos: list[tuple[int, int]] = []

    width: int = len(map[0])
    height: int = len(map)

    while (not started) or count_loop > 0:
        started = True
        count_loop = 0
        for i in range(height):
            for j in range(width):
                if map[i][j] != "@":
                    continue

                num_adj = count_adjacent_positions(map, j, i)
                if num_adj < 4:
                    remove_pos.append((j, i))
                    count_loop += 1

        count += count_loop
        for pos in remove_pos:
            map[pos[1]][pos[0]] = "x"

        print(f"Removed {count_loop} rolls.")
        _ = print_map(map)

    return count


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
