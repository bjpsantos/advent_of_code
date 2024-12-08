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

    def get_successive_differences(self, report):
        # report = report.split()
        report = list(map(int, report))
        diff = list(map(lambda x, y: x - y, report[:-1], report[1:]))
        return diff

    def check_all_levels_decreasing(self, diff):
        decreasing_results = [x > 0 for x in diff]
        decreasing = all(decreasing_results)
        return decreasing, decreasing_results

    def check_all_levels_increasing(self, diff):
        increasing_results = [x < 0 for x in diff]
        increasing = all(increasing_results)
        return increasing, increasing_results

    def levels_diff_between_1_and_3(self, diff):
        results = [(abs(x) >= 1 and abs(x) <= 3) for x in diff]
        return all(results), results

    def check_numb_safe_reports(self, reports, apply_dampner=False):
        n_safe = 0
        for report in reports:
            report = report.split()
            diff = self.get_successive_differences(report)

            safe = (
                self.check_all_levels_decreasing(diff)[0]
                or self.check_all_levels_increasing(diff)[0]
            ) and self.levels_diff_between_1_and_3(diff)[0]
            if safe:
                n_safe += 1

            else:  # not safe
                if apply_dampner:
                    if self.safe_with_problem_dampner(report, diff):
                        print("report that is safe by dampner:", report)
                        n_safe += 1

        return n_safe

    def safe_with_problem_dampner(self, non_safe_report, diff):
        _, decreasing_results = self.check_all_levels_decreasing(diff)
        _, increasing_results = self.check_all_levels_increasing(diff)
        _, values_results = self.levels_diff_between_1_and_3(diff)

        idx_with_issues = set()
        if decreasing_results.count(False) == 1:
            [
                idx_with_issues.add(i)
                for i, val in enumerate(decreasing_results)
                if not val
            ]
        if increasing_results.count(False) == 1:
            [
                idx_with_issues.add(i)
                for i, val in enumerate(increasing_results)
                if not val
            ]
        if values_results.count(False) == 1:
            [idx_with_issues.add(i) for i, val in enumerate(values_results) if not val]

        if len(idx_with_issues) > 2:
            return False
        else:
            # remove report idx
            for idx in idx_with_issues:
                dampned_report = non_safe_report.copy()
                dampned_report.pop(idx)
                diff = self.get_successive_differences(dampned_report)

                safe = (
                    self.check_all_levels_decreasing(diff)[0]
                    or self.check_all_levels_increasing(diff)[0]
                ) and self.levels_diff_between_1_and_3(diff)[0]
                safe
                if safe:
                    return True
                else:
                    # the issue could be in the next idx
                    dampned_report = non_safe_report.copy()
                    dampned_report.pop(idx + 1)
                    diff = self.get_successive_differences(dampned_report)

                    safe = (
                        self.check_all_levels_decreasing(diff)[0]
                        or self.check_all_levels_increasing(diff)[0]
                    ) and self.levels_diff_between_1_and_3(diff)[0]
                    if safe:
                        return True
            return False

    def solve(self, part):
        if part == 1:
            return self.check_numb_safe_reports(self.input)
        elif part == 2:
            return self.check_numb_safe_reports(self.input, apply_dampner=True)


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]

    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 2
    assert main(raw=files["test"], part=2) == 4

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
