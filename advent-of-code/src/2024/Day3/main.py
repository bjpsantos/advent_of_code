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
        self.input = "".join(text_input)

        self.regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        self.regex_pattern_cond = r"mul\((\d{1,3}),(\d{1,3})\)|(do|don\'t)\(\)"

    def get_sections(self, pattern):
        sections = re.findall(pattern, self.input)
        return sections

    def sum_mul_sections(self, mul_sections):
        result = 0
        for section in mul_sections:
            result = result + int(section[0]) * int(section[1])

        return result

    def conditional_sum_sections(self, sections):
        enable = True

        result = 0
        for section in sections:
            if section[2] == "don't":
                enable = False
            elif section[2] == "do":
                enable = True
            else:
                if enable:
                    result = result + int(section[0]) * int(section[1])

        return result

    def solve(self, part):
        if part == 1:
            mul_sections = self.get_sections(pattern=self.regex_pattern)
            return self.sum_mul_sections(mul_sections)

        if part == 2:
            sections = self.get_sections(pattern=self.regex_pattern_cond)
            return self.conditional_sum_sections(sections)


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]

    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 161
    assert main(raw=files["test2"], part=2) == 48

    # solutions
    print(f"\nRunning Solutions:")
    assert main(raw=files["input"], part=1) == 179571322


def solve():
    print(f"\nSolving:")
    answer1 = main(raw=files["input"], part=1)
    print(f"Answer part1: {magenta_color}{answer1}{reset_color}")
    answer2 = main(raw=files["input"], part=2)
    print(f"Answer part2: {magenta_color}{answer2}{reset_color}")


if __name__ == "__main__":
    run_tests()
    solve()
