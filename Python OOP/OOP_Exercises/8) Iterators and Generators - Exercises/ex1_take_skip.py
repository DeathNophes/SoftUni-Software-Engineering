class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.iterations += 1
        if self.iterations < self.count:
            return self.iterations * self.step
        raise StopIteration
