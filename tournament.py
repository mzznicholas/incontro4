import random

from queue import Queue
from typing import Tuple


class Team:
    def __init__(self, name: str, exp: int):
        pass

    def __str__(self) -> str:
        pass

    def __lt__(self, other) -> bool:
        pass


class Tournament:
    def __init__(self):
        self.teams = None # sostituisci None con una coda

    def register_team(self, team: Team):
        pass

    def is_finished(self) -> bool:
        pass

    def get_winner(self):
        pass

    def get_next_two_teams(self) -> Tuple[Team]:
        pass

    def play_match(self, team1, team2) -> Team:
        pass


def main():
    random.seed(8)
    t = Tournament()
    t.register_team(Team("A", 10))
    t.register_team(Team("B", 20))
    t.register_team(Team("C", 30))
    t.register_team(Team("D", 5))
    t.register_team(Team("E", 15))

    while not t.is_finished():
        teams = t.get_next_two_teams()
        print(f"{teams[0]} vs {teams[1]}")
        w = t.play_match(teams[0], teams[1])
        print(f"Match winner: {w}")
        print("-" * 10)

    print(f"Tournament winner: {t.get_winner()}")


if __name__ == '__main__':
    main()
