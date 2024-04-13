from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


class Tournament:
    VALID_EQUIPMENT = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAMS = {
        "IndoorTeam": IndoorTeam,
        "OutdoorTeam": OutdoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            equipment = self.VALID_EQUIPMENT[equipment_type]()
        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        except KeyError:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment_list = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        if team.budget < self.VALID_EQUIPMENT[equipment_type].PRICE:
            raise Exception("Budget is not enough!")

        index = self.equipment.index(equipment_list[-1])
        sold_equipment = self.equipment.pop(index)

        team.equipment.append(sold_equipment)
        team.budget -= sold_equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_list = [e for e in self.equipment if e.__class__.__name__ == equipment_type]

        for item in equipment_list:
            item.increase_price()

        return f"Successfully changed {len(equipment_list)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = [t for t in self.teams if t.name == team_name1][0]
        team2 = [t for t in self.teams if t.name == team_name2][0]

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_protection = sum([e.protection for e in team1.equipment])
        team2_protection = sum([e.protection for e in team2.equipment])

        team1_result = team1_protection + team1.advantage
        team2_result = team2_protection + team2.advantage

        if team1_result == team2_result:
            return "No winner in this game."

        if team1_result > team2_result:
            team1.win()
            return f"The winner is {team1.name}."

        if team1_result < team2_result:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):
        result = f"Tournament: {self.name}\n" + \
                f"Number of Teams: {len(self.teams)}\n" + \
                f"Teams:\n"

        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)

        for team in sorted_teams:
            result += f"{team.get_statistics()}\n"

        return result[:-1]
