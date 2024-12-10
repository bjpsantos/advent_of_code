from utils.tools import get_txt_files, read_input, timing_decorator
from utils.colors import magenta_color, reset_color

import re

import numpy as np

files = get_txt_files(__file__)
#########
# Start #
#########


class Puzzle:
    def __init__(self, text_input):
        self.input = text_input
        self.input = [list(string) for string in self.input]
        self.n_rows = len(self.input)
        self.n_cols = len(self.input[0])

        self.all_directions = [
            (0, 1),  # Vertical, bottom to top
            (0, -1),  # Vertical, top to bottom
            (1, 0),  # Horizontal, left to right
            (-1, 0),  # Horizontal, right to left
            (1, 1),  # Diagonal, bottom to top, left to right
            (1, -1),  # Diagonal, top to bottom, left to right
            (-1, 1),  # Diagonal, bottom to top, right to left
            (-1, -1),  # Diagonal, top to bottom, right to left
        ]

        self.word = list("XMAS")
        self.first_letter = self.word[0]

        self.directions_X = [
            (1, 1),  # Diagonal, bottom to top, left to right
            (1, -1),  # Diagonal, top to bottom, left to right
            (-1, 1),  # Diagonal, bottom to top, right to left
            (-1, -1),  # Diagonal, top to bottom, right to left
        ]

        self.word_2 = list("MAS")
        self.middle_letter = self.word_2[1]

    def search_from_current_cell(self, row, col, direction):
        # returns True if it finds the word
        found_word = ""
        for i in range(len(self.word)):
            current_row = row + i * direction[0]
            current_col = col + i * direction[1]

            if (
                current_row < 0
                or current_row >= self.n_rows
                or current_col < 0
                or current_col >= self.n_cols
            ):
                continue
            elif self.input[current_row][current_col] != self.word[i]:
                return False
            else:
                found_word = found_word + self.input[current_row][current_col]

        if found_word == "".join(self.word):
            return True
        else:
            return False

    def search_from_current_cell_X(self, row, col, direction):
        found_word = ""
        for i in range(len(self.word_2)):
            current_row = row + i * direction[0] - direction[0]
            current_col = col + i * direction[1] - direction[1]

            if (
                current_row < 0
                or current_row >= self.n_rows
                or current_col < 0
                or current_col >= self.n_cols
            ):
                continue
            elif self.input[current_row][current_col] != self.word_2[i]:
                # test = self.input[current_row][current_col]
                return False
            else:
                # test2 =  self.input[current_row][current_col]
                found_word = found_word + self.input[current_row][current_col]

        if found_word == "".join(self.word_2):
            return True
        else:
            return False

    def find_word(
        self,
    ):
        n_found_words = 0
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if self.input[row][col] == self.first_letter:
                    for direction in self.all_directions:
                        if self.search_from_current_cell(row, col, direction):
                            n_found_words += 1

        return n_found_words

    def find_word_X(self):
        n_found_X = 0
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if self.input[row][col] == self.middle_letter:
                    n_MAS = 0
                    for direction in self.directions_X:
                        if self.search_from_current_cell_X(row, col, direction):
                            n_MAS += 1

                    if n_MAS == 2:
                        n_found_X += 1

        return n_found_X

    def solve(self, part):
        if part == 1:
            return self.find_word()

        if part == 2:
            return self.find_word_X()


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]

    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 18
    assert main(raw=files["test2"], part=2) == 1
    assert main(raw=files["test"], part=2) == 9

    # solutions
    print(f"\nRunning Solutions:")
    assert main(raw=files["input"], part=1) == 2557


def solve():
    print(f"\nSolving:")
    answer1 = main(raw=files["input"], part=1)
    print(f"Answer part1: {magenta_color}{answer1}{reset_color}")
    answer2 = main(raw=files["input"], part=2)
    print(f"Answer part2: {magenta_color}{answer2}{reset_color}")


if __name__ == "__main__":
    run_tests()
    solve()
