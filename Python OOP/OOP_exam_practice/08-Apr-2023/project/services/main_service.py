from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        result = f"{self.name} Main Service:\nRobots: "

        if self.robots:
            robot_names = [r.name for r in self.robots]
            result += ' '.join(robot_names)
        else:
            result += 'none'

        return result