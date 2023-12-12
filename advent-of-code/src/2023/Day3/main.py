from utils.tools import get_txt_files, read_input, timing_decorator
from utils.colors import magenta_color, reset_color
import re

files = get_txt_files(__file__)
#########
# Start #
#########


class Puzzle:
    def __init__(self, text_input):
        self.input = text_input
        self.pattern = re.compile(r"[0-9.]")

    def parse_input(self):
        # parsed_input = [char for line in self.input for char in line ]
        self.parsed_input = [list(line) for line in self.input]
        return self.parsed_input

    def check_surrounderings(self, x, y):
        keep = False
        for j in [y - 1, y, y + 1]:
            for i in [x - 1, x, x + 1]:
                if (
                    j >= 0
                    and j < len(self.parsed_input)
                    and i >= 0
                    and i < len(self.parsed_input[0])
                ):
                    # print(len(self.parsed_input))
                    # print(len(self.parsed_input[0]))
                    if not self.pattern.match(
                        self.parsed_input[j][i]
                    ):  # if there is a symbol adjacent to this number
                        keep = True

        return keep
        # True if there is a number/symbol
        # False if there isn't

    def get_mask_adjacent(self, parsed_input):
        y_len = len(parsed_input)
        x_len = len(parsed_input[0])
        mask = []
        r = range(y_len)
        for y in range(y_len):
            row = []
            for x in range(x_len):
                if parsed_input[y][x].isnumeric():
                    keep = self.check_surrounderings(x, y)
                else:
                    keep = False
                row.append(keep)
            mask.append(row)

        return mask

    def get_part_numbers(self, mask, parsed_input):
        keep_numbers = []
        l = len(parsed_input)
        for y in range(len(parsed_input)):
            numb = ""
            keep_numb = False
            for x in range(len(parsed_input[0])):
                if parsed_input[y][x].isnumeric():
                    numb = numb + parsed_input[y][x]
                    if mask[y][x] == True:
                        keep_numb = True
                else:
                    if keep_numb:  # we have to keep the previous found number
                        keep_numbers.append(int(numb))
                    numb = ""
                    keep_numb = False

            if (
                keep_numb
            ):  # to make sure we don't forget the numbers right at the end of the line
                keep_numbers.append(int(numb))

        return keep_numbers

    def solve(self, part):
        if part == 1:
            parsed_input = self.parse_input()
            mask = self.get_mask_adjacent(parsed_input)
            part_numbers = self.get_part_numbers(mask, parsed_input)

            return sum(part_numbers)
        if part == 2:
            pass


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]
    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 4361
    assert main(raw=files["test2"], part=1) == 567 + 927
    assert main(raw=files["test3"], part=1) == 413
    # assert main(raw=files["test2"], part=2) == 281

    # solutions
    # print(f"\nRunning Solutions:")
    # assert main(raw=files["input"], part=1) == 55971
    # assert main(raw=files["input"], part=2) == 54719


def solve():
    print(f"\nSolving:")
    answer1 = main(raw=files["input"], part=1)
    print(f"Answer part1: {magenta_color}{answer1}{reset_color}")
    # answer2 = main(raw=files["input"], part=2)
    # print(f"Answer part2: {magenta_color}{answer2}{reset_color}")


if __name__ == "__main__":
    run_tests()
    solve()
