class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        reversed_data = sorted(self.data, reverse=True)
        return f"[{', '.join(reversed_data)}]"