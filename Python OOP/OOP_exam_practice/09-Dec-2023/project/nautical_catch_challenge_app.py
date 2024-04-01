from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    VALID_DIVERS_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    VALID_FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.VALID_DIVERS_TYPES[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.has_health_issue = True
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            diver.has_health_issue = True

            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0

        divers_with_health_issues = [d for d in self.divers if d.has_health_issue]
        for d in divers_with_health_issues:
            d.oxygen_level = d.INITIAL_OXYGEN_LEVEL
            d.has_health_issue = False
            count += 1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        result = f"**{diver_name} Catch Report**\n"

        diver = next(filter(lambda d: d.name == diver_name, self.divers))

        for fish in diver.catch:
            result += f"{fish.fish_details()}\n"

        return result[:-1]

    def competition_statistics(self):
        result = f"**Nautical Catch Challenge Statistics**\n"

        sorted_divers = sorted(
            self.divers,
            key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        sorted_healthy_divers = [d for d in sorted_divers if not d.has_health_issue]

        for diver in sorted_healthy_divers:
            result += f"{diver}\n"

        return result[:-1]
