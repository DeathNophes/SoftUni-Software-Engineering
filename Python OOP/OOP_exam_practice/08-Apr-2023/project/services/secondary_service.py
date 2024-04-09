from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        result = f"{self.name} Secondary Service:\nRobots: "

        if self.robots:
            robot_names = [r.name for r in self.robots]
            result += ' '.join(robot_names)
        else:
            result += 'none'

        return result