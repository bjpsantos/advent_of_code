from utils.tools import get_txt_files, read_input, timing_decorator
from utils.colors import magenta_color, reset_color


import numpy as np

files = get_txt_files(__file__)
#########
# Start #
#########


class Puzzle:
    def __init__(self, text_input):
        self.input = text_input
        self.spelled_out = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]

        # for i, written in enumerate(self.spelled_out)
        self.mapper = {written: i + 1 for i, written in enumerate(self.spelled_out)}

    def get_numbers(self):
        aux_list = []
        for line in self.input:
            aux = ""
            for char in line:
                if str.isnumeric(char):
                    aux = aux + char

            aux_list.append(int(aux[0] + aux[-1]))
        return aux_list

    def get_numbers2(self):
        aux_list = []
        for line in self.input:
            list_idx = []
            list_numbers = []
            for written in self.spelled_out:
                idx = line.find(written)
                if idx != -1:
                    list_idx.append(idx)
                    list_numbers.append(self.mapper[written])
                idx_r = line.rfind(written)
                if idx_r != -1:
                    list_idx.append(idx_r)
                    list_numbers.append(self.mapper[written])

            for idx, char in enumerate(line):
                if str.isnumeric(char):
                    list_idx.append(idx)
                    list_numbers.append(int(char))

            array_idx = np.array(list_idx)
            array_numb = np.array(list_numbers)

            sorted_idx = array_idx.argsort()
            sorted_numb = array_numb[sorted_idx]

            aux_list.append(int(str(sorted_numb[0]) + str(sorted_numb[-1])))

        return aux_list

    def solve(self, part):
        if part == 1:
            list_numbers = self.get_numbers()
            return sum(list_numbers)

        if part == 2:
            return sum(self.get_numbers2())


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]
    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 142
    assert main(raw=files["test2"], part=2) == 281
    assert main(raw=files["test3"], part=2) == 33

    # solutions
    print(f"\nRunning Solutions:")
    # assert main(raw=files["input"], part=1) == 55971
    # assert main(raw=files["input"], part=2) == 54719


def solve():
    print(f"\nSolving:")
    answer1 = main(raw=files["input"], part=1)
    print(f"Answer part1: {magenta_color}{answer1}{reset_color}")
    answer2 = main(raw=files["input"], part=2)
    print(f"Answer part2: {magenta_color}{answer2}{reset_color}")


if __name__ == "__main__":
    run_tests()
    solve()
