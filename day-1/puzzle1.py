import os
from typing import Tuple
from pathlib import Path

def change_value(curr_num: int, change_val: int) -> Tuple[int, int]:
    new_num: int = (curr_num + change_val) % 100
    zeros_clicked: int = 0
    return (new_num, zeros_clicked)

def parse_input(input_line: str) -> int:
    input_line_clean: str = input_line.strip().strip('\n')
    direction: str = input_line_clean[0].lower()
    number: int = int(input_line_clean[1:])

    if direction == "l":
        number = number * -1
    
    return number

def solve_puzzle(file: str) -> int:
    with open(file, "r") as f:
        inputs: list[str] = f.readlines()
    
    zero_count: int = 0
    curr_num: int = 50
    for input in inputs: 
        change_val: int = parse_input(input)
        curr_num, zero_clicked = change_value(curr_num, change_val)
        
        if curr_num == 0:
            zero_count += 1
    
    return zero_count

def main():
    file_input: Path = Path(__file__).parent.resolve() / "input.txt"
    password: int = solve_puzzle(file_input)
    print(f"The password is {password}!")
    return 0

if __name__ == "__main__":
    main()