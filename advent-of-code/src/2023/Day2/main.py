from utils.tools import get_txt_files, read_input, timing_decorator
from utils.colors import magenta_color, reset_color

files = get_txt_files(__file__)
#########
# Start #
#########


class Game:
    def __init__(self, name):
        self.name = name
        self.id = int(name.split(" ")[-1])
        self.plays = []

    def add_play(self, play):
        red = 0
        blue = 0
        green = 0
        for x in play.split(","):
            if "red" in x:
                red = int(x.split()[0])
            elif "blue" in x:
                blue = int(x.split()[0])
            elif "green" in x:
                green = int(x.split()[0])
        self.plays.append(Play(red, green, blue))

    def check_game_meets_criteria(self, max_blue, max_green, max_red):
        flag = True
        for play in self.plays:
            if play.blue > max_blue or play.green > max_green or play.red > max_red:
                flag = False
                break

        return flag

    def get_power_min_set_of_cubes(
        self,
    ):
        red = 0
        blue = 0
        green = 0
        for play in self.plays:
            if play.red > red:
                red = play.red
            if play.blue > blue:
                blue = play.blue
            if play.green > green:
                green = play.green

        return red * blue * green


class Play:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Puzzle:
    def __init__(self, text_input):
        self.input = text_input

    def parse_input(self):
        games = []
        for game_info in self.input:
            g = Game(game_info.split(":")[0])
            plays = game_info.split(":")[1].split(";")
            [g.add_play(play) for play in plays]

            games.append(g)

        return games

    def select_possible_games(self, max_red, max_green, max_blue, games):
        possible_games = []

        [
            possible_games.append(game)
            for game in games
            if game.check_game_meets_criteria(
                max_blue=max_blue, max_green=max_green, max_red=max_red
            )
        ]

        return possible_games

    def solve(self, part):
        if part == 1:
            parsed_input = self.parse_input()
            possible_games = self.select_possible_games(
                max_red=12, max_green=13, max_blue=14, games=parsed_input
            )
            ids = [game.id for game in possible_games]
            return sum(ids)

        if part == 2:
            parsed_input = self.parse_input()

            return sum([game.get_power_min_set_of_cubes() for game in parsed_input])


@timing_decorator
def main(raw, part):
    text_input = read_input(raw)
    input_parsed = [i if i else "" for i in text_input]
    puzzle = Puzzle(input_parsed)
    return puzzle.solve(part)


def run_tests():
    print(f"\nRunning Tests:")
    assert main(raw=files["test"], part=1) == 8
    assert main(raw=files["test"], part=2) == 2286

    # solutions
    print(f"\nRunning Solutions:")
    assert main(raw=files["input"], part=1) == 1931
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
