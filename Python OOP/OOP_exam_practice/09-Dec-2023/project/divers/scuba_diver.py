from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        if self.oxygen_level >= time_to_catch:
            self.oxygen_level -= (0.3 * time_to_catch)
            self.oxygen_level = round(self.oxygen_level)
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN_LEVEL