class Task:
    def __init__(self, name: str, due_date: str, completed=False):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = completed

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return new_date

    def add_comment(self, new_comment: str):
        self.comments.append(new_comment)

    def edit_comment(self, comment_idx: int, new_comment: str):
        if not 0 <= comment_idx < len(self.comments):
            return "Cannot find comment."

        self.comments[comment_idx] = new_comment
        return ', '.join(self.comments)

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
