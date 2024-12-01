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

    def create_lists(self):
        list_A = []
        list_B = []
        for row in self.input:
            split_row = row.split()
            list_A.append(int(split_row[0]))
            list_B.append(int(split_row[1]))
        
        list_A = sorted(list_A)
        list_B = sorted(list_B)

        return list_A, list_B

    def find_distances(self, list_A, list_B):
        distances = []
        for i in range(len(list_A)):
            distances.append(abs(list_A[i] - list_B[i]))
        return distances
    
    def get_similarity_score(self, list_A, list_B):
        similarity_score = []
        for i in list_A:
            similarity_score.append(i*list_B.count(i))

        return similarity_score
        

    def solve(self, part):
        if part == 1:
            list_A, list_B = self.create_lists()
            distances = self.find_distances(list_A, list_B)
            return sum(distances)

        if part == 2:
            list_A, list_B = self.create_lists()
            similarity_score = self.get_similarity_score(list_A, list_B)
            return sum(similarity_score)


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]
    
    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 11
    assert main(raw=files["test"], part=2) == 31

    # solutions
    print(f"\nRunning Solutions:")
    # assert main(raw=files["input"], part=1) == 55971



def solve():
    print(f"\nSolving:")
    answer1 = main(raw=files["input"], part=1)
    print(f"Answer part1: {magenta_color}{answer1}{reset_color}")
    answer2 = main(raw=files["input"], part=2)
    print(f"Answer part2: {magenta_color}{answer2}{reset_color}")


if __name__ == "__main__":
    run_tests()
    solve()
