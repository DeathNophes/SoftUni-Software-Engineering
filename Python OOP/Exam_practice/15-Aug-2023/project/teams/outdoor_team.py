from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET = 1000.0
    ADVANTAGE_INCREASE_PER_WIN = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, OutdoorTeam.INITIAL_BUDGET)

    def win(self):
        self.wins += 1
        self.advantage += OutdoorTeam.ADVANTAGE_INCREASE_PER_WIN