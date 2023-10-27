class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
        # It is not different than 'sender', that is why we add 'self.'


emails_objects = []

info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    emails_objects.append(email_info)
    info = input()
# Everytime we create the same object, but with different data
# Then we save them as objects in emails_objects

indexes = [int(index) for index in input().split(", ")]

for index in indexes:
    emails_objects[index].send()
for current_email in emails_objects:
    print(current_email.get_info())
